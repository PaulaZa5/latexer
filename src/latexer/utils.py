from loguru import logger


class Cleaner(object):

    def __init__(self, expression):

        self._expression = expression

        self._check_spaces(in_place=True)
        self._check_negatives(in_place=True)
        self._check_apostrophes(in_place=True)
        self._check_dots(in_place=True)
        # self._check_mul(in_place=True)
        self._check_powers(in_place=True)

    def _check_apostrophes(self, in_place=False):

        expr = self._expression

        for apostrophe in ['`', '‘', '"', "'"]:
            if apostrophe in expr:
                removable = []
                alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

                for i, c in enumerate(expr):
                    if c == apostrophe:
                        if expr[i-1] not in alpha or i == 0 or i == len(expr)-1:
                            removable.append(i)

                for i in reversed(removable):
                    expr = expr[:i] + expr[i+1:]
                    logger.debug('Removed `{}` at index {}.'.format(apostrophe, i))

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_dots(self, in_place=False):

        expr = self._expression

        if '.' in expr:
            removable = []
            nums = '0123456789'

            for i, c in enumerate(expr):
                if c == '.':
                    if expr[i-1] not in nums or expr[i+1] not in nums or i == 0 or i == len(expr)-1:
                        removable.append(i)

            for i in reversed(removable):
                expr = expr[:i] + expr[i+1:]
                logger.debug('Removed `.` at index {}.'.format(i))

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_mul(self, in_place=False):

        expr = self._expression

        insertable = []
        nums = '0123456789'
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz([{'

        for i, c in enumerate(expr):
            if c in alpha and i != 0:
                if expr[i-1] in nums:
                    insertable.append(i)

        for i in reversed(insertable):
            expr = expr[:i] + '*' + expr[i:]
            logger.debug('Inserted `*` at index {}.'.format(i))

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_negatives(self, in_place=False):

        expr = self._expression.replace('—', '-')

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_powers(self, in_place=False):

        expr = self._expression

        insertable = []
        nums = '0123456789'
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz)]}'

        for i, c in enumerate(expr):
            if c in alpha and i != len(expr)-1:
                if expr[i+1] in nums:
                    insertable.append(i+1)

        for i in reversed(insertable):
            expr = expr[:i] + '^' + expr[i:]
            logger.debug('Inserted `^` at index {}.'.format(i))

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_spaces(self, in_place=False):

        expr = self._expression.replace(' ', '')

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def __repr__(self):

        return self._expression

class Latexer(object):

    def __init__(self, cleaner):

        expr = str(cleaner).split('\n')

        if len(expr) == 1:
            self.top = ''
            self._expression = expr[0]
            self.bottom = ''
        elif len(expr) == 2:
            self.top = expr[0]
            self._expression = expr[1]
            self.bottom = ''
        elif len(expr) == 3:
            self.top = expr[0]
            self._expression = expr[1]
            self.bottom = expr[2]

        self._check_dev(in_place=True)
        self._check_summation(in_place=True)
        self._check_int(in_place=True)
        self._check_powers(in_place=True)
        self._inline_latex(in_place=True)
        self._assert_parentheses()
        # self._assert_latex_compatibility()

    def _assert_latex_compatibility(self):

        from latex import build_pdf, LatexBuildError

        try:
            build_pdf('\\documentclass{article}\\begin{document}\n'+self._expression+'\n\\end{document}')
        except LatexBuildError as e:
            for err in e.get_errors():
                logger.error('Error in {}, line {}: {}'.format(err['filename'], err['line'], err['error']))

    def _assert_parentheses(self):

        lparen, rparen = {'(': 1, '[': 2, '{': 3}, {')': 1, ']': 2, '}': 3}
        parens = []

        for c in self._expression:
            if c in lparen:
                parens.append(c)
            elif c in rparen:
                assert rparen[c] == lparen[parens.pop()], logger.error('Incorrect parentheses type at {}.'.format(c))

        assert len(parens) == 0, logger.error('Found non-closed parentheses.')

    def _check_dev(self, in_place=False):

        expr = self._expression

        special_chars = ('*', '+', '-')
        lparen, rparen = ('(', '[', '{'), (')', ']', '}')
        chars_levels = [0]
        fracts = [[0,0,0]]

        for i, c in enumerate(expr):

            if c in ('/', '÷'):
                fracts.append([chars_levels[-1], i, None])
            elif c in special_chars:
                chars_levels[-1] = i+1

                if fracts[-1][-1] is None:
                    fracts[-1][-1] = i
            elif c in lparen:
                chars_levels[-1] = i+1
                chars_levels.append(i+1)
                fracts.append([0,0,0])
            elif c in rparen:
                chars_levels.pop()
                if fracts[-1][-1] is None:
                    fracts[-1][-1] = i

        for start, mid, finish in reversed(fracts):

            if start == mid == finish:
                continue

            expr = expr[:start] + '\\frac{}{}'.format('{' + expr[start:mid] + '}', '{' + expr[mid+1:finish] + '}') + expr[finish:]

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_int(self, in_place=False):

        expr = '\\int^{}_{} '.format('{' + self.bottom + '}', '{' + self.top + '}') + self._expression[1:] if self._expression[0] in (['I', 'J', '[', ']']) else self._expression

        if expr != self._expression:
            self.top = ''

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_powers(self, in_place=False):

        expr = self._expression

        if self.top != '':
            expr = expr + '^' + self.top
            logger.debug('Inserted `^{}` at the end of the expression.'.format(self.top))
            self.top = ''

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _check_summation(self, in_place=False):

        expr = '\\sum^{}_{} '.format('{' + self.bottom + '}', '{' + self.top + '}') + self._expression[1:] if self._expression[0] in (['S']) else self._expression

        if expr != self._expression:
            self.top = ''

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def _inline_latex(self, in_place=False):

        expr = '$' + self._expression + '$'

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self._expression, expr))

        if in_place:
            self._expression = expr

        return expr

    def __repr__(self):

        return self._expression


if __name__ == '__main__':

    for expr in ['sin (4x+2)', 'y =(-1x /3)+(3x./6) ‘', '2\n(x3+2x2—3x+2)']:

        print(Latexer(Cleaner(expr)))

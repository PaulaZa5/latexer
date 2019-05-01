from loguru import logger


class Cleaner(object):

    def __init__(self, expression):

        self.expression = expression

        self._check_spaces(in_place=True)
        self._check_negatives(in_place=True)
        self._check_apostrophes(in_place=True)
        self._check_dots(in_place=True)
        # self._check_mul(in_place=True)
        self._check_powers(in_place=True)

    def _check_apostrophes(self, in_place=False):

        expr = self.expression

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

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_dots(self, in_place=False):

        expr = self.expression

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

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_mul(self, in_place=False):

        expr = self.expression

        insertable = []
        nums = '0123456789'
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        for i, c in enumerate(expr):
            if c in alpha and i != len(expr)-1:
                if expr[i-1] in nums:
                    insertable.append(i)

        for i in reversed(insertable):
            expr = expr[:i] + '*' + expr[i:]
            logger.debug('Inserted `*` at index {}.'.format(i))

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_negatives(self, in_place=False):

        expr = self.expression.replace('—', '-')

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_powers(self, in_place=False):

        expr = self.expression

        insertable = []
        nums = '0123456789'
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        for i, c in enumerate(expr):
            if c in alpha and i != len(expr)-1:
                if expr[i+1] in nums:
                    insertable.append(i+1)

        for i in reversed(insertable):
            expr = expr[:i] + '^' + expr[i:]
            logger.debug('Inserted `^` at index {}.'.format(i))

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_spaces(self, in_place=False):

        expr = self.expression.replace(' ', '')

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def __repr__(self):

        return self.expression

class Latexer(object):

    def __init__(self, cleaner):

        expr = cleaner.expression.split('\n')

        if len(expr) == 1:
            self.top = ''
            self.expression = expr[0]
            self.bottom = ''
        elif len(expr) == 2:
            self.top = expr[0]
            self.expression = expr[1]
            self.bottom = ''
        elif len(expr) == 3:
            self.top = expr[0]
            self.expression = expr[1]
            self.bottom = expr[2]

        self._check_summation(in_place=True)
        self._check_int(in_place=True)
        self._check_powers(in_place=True)
        self._inline_latex(in_place=True)
        self._assert_parentheses()
        self._assert_latex_compatibility()

    def _assert_latex_compatibility(self):

        from latex import build_pdf, LatexBuildError

        try:
            build_pdf('\\documentclass{article}\\begin{document}\n'+self.expression+'\n\\end{document}')
        except LatexBuildError as e:
            for err in e.get_errors():
                logger.error('Error in {}, line {}: {}'.format(err['filename'], err['line'], err['error']))

    def _assert_parentheses(self):

        for lparen, rparen in [('(', ')'), ('[', ']'), ('{', '}')]:
            if self.expression.count(lparen) != self.expression.count(rparen):
                logger.error('Count of `{}` != count of `{}`.'.format(lparen, rparen))

    def _check_int(self, in_place=False):

        expr = '\\int_{}^{} '.format('{' + self.top + '}', '{' + self.bottom + '}') + self.expression[1:] if self.expression[0] in (['I', 'J', '[', ']']) else self.expression

        if expr != self.expression:
            self.top = ''

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_powers(self, in_place=False):

        expr = self.expression

        if self.top != '':
            expr = expr + '^' + self.top
            logger.debug('Inserted `^{}` at the end of the expression.'.format(self.top))
            self.top = ''

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _check_summation(self, in_place=False):

        expr = '\\sum_{}^{} '.format('{' + self.top + '}', '{' + self.bottom + '}') + self.expression[1:] if self.expression[0] in (['S']) else self.expression

        if expr != self.expression:
            self.top = ''

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def _inline_latex(self, in_place=False):

        expr = '$' + self.expression + '$'

        logger.debug('expr.old=`{}` and expr.new=`{}`.'.format(self.expression, expr))

        if in_place:
            self.expression = expr

        return expr

    def __repr__(self):

        return self.expression


if __name__ == '__main__':

    for expr in ['sin (4x+2)', 'y =(—1x‘/3)+(3 x/ 6)', 'y =(-1x /3)+(3x./6) ‘',
                 '2\n(x3+2x2—3x+2)']:

        print(Latexer(Cleaner(expr)))

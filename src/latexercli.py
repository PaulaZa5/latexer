from argparse import ArgumentParser

from loguru import logger
import pytesseract

from utils import Cleaner, Latexer


if __name__ == '__main__':

    parser = ArgumentParser(description='Turn your equation image into inline LaTeX expression.')
    parser.add_argument('--image', '-im', type=str, required=True, help='Input Image')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show debugging data.')
    args = parser.parse_args()

    if not args.verbose:

        logger.disable('utils')
        logger.disable('__main__')

    try:
        expr = pytesseract.image_to_string(args.image, lang='eng', output_type=pytesseract.Output.DICT)['text']
        logger.debug('Opened {}.'.format(args.image))
    except:
        logger.error('Failed to open {}, make sure you\'ve installed the tesseract-ocr.'.format(args.image))
        exit('Failed to open {}, make sure you\'ve installed the tesseract-ocr.')

    res = Latexer(Cleaner(expr))
    print(res)

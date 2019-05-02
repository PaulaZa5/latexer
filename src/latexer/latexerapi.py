from flask import Flask , request
from loguru import logger
import pytesseract

from utils import Cleaner, Latexer

app = Flask(__name__)

@app.route("/latexer")
def latexerapi():
    image = request.args.get("image")
    try:
        expr = pytesseract.image_to_string(image, lang='eng', output_type=pytesseract.Output.DICT)['text']
        logger.debug('Opened {}.'.format(image))
    except:
        logger.error('Failed to open {}.'.format(image))
        return ''

    return str(Latexer(Cleaner(expr)))

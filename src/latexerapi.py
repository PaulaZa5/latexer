import json

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
        logger.error('Failed to open {}, make sure you\'ve installed the tesseract-ocr.'.format(image))
        return json.dumps({'image': image, 'status': 'failed', 'latex': ''}, indent=4)

    res = Latexer(Cleaner(expr))
    return json.dumps({'image': image, 'status': res.status, 'latex': str(res)}, indent=4)


if __name__ == '__main__':
    app.run()

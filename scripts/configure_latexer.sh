#!/bin/sh
#
# NAME: CONFIG LATEXER


echo "Installing required python packages..."

if ! which pip3 > /dev/null; then
    echo -e "pip3 not found! install it? (Y/n) \c"
    read
    if "$REPLY" = "n"; then
        exit 0
    fi
    apt install pip3
fi

pip install flask latex loguru pytesseract

echo "Installed required python packages succesfully."


echo "Installing required software components..."

apt install latexmk tesseract-ocr=3 -y

echo "Installed required software components."


exit 0

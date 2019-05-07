<p align="center">
  <h1 align="center"> LaTeXer </h1>
</p>

<p align="center">
  <b>Turn your handwritten equations</b> into <i>LaTeX</i>!
</p>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Testing](#testing)
- [To Do](#to-do)

---

## Description

Application to help you turn your handwritten mathmatical equations into inline LaTeX code.
<br>

## Testing

1. Clone and configure your environment
  ```bash
  git clone https://github.com/BoulaZa5/latexer
  cd latexer
  bash ./scripts/configure_latexer.sh
  ```
2. Try the command line interface
  ```bash
  python3 ./src/latexercli.py --image ./data/1.jpg
  ```
3. Try the JSON request API
  ```bash
  python3 ./src/latexerapi.py
  firefox http://127.0.0.1:5000/latexer?image=./data/1.jpg
  ```
4. Try the Web Application

    You need to have php, nodejs installed on your machine
      ```bash
      cd beta
      php -S localhost:8000
      ```
      open another terminal in the master branch
      ```bash
      cd latexConverter
      node server.js
      ```
      open another terminal in the master branch
      ```bash
      cd src/latexer/
      export FLASK_APP=latexerapi.py
      flask run
      node server.js
      ```

      ```bash
      python3 ./src/latexerapi.py
      ```
<br>

## To Do
* [ ] Image Preprocessing
* [x] OCR
* [x] OCR output cleaner
* [x] String equation to LaTeX
* [ ] String equation parser
* [ ] Parsetree to LaTeX
* [x] CLI
* [x] API
* [x] Web Application
* [ ] Desktop Application
* [ ] Mobile Application

<br>

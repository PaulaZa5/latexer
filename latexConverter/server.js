var express = require("express");
var bodyParser = require("body-parser");
var tex2svg = require( 'tex-equation-to-svg' );
var app = express();

const mjpage = require('mathjax-node-page');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    );
    res.setHeader(
        "Access-Control-Allow-Methods",
        "GET, POST, PATCH, DELETE, OPTIONS"
    );
    next();
});

app.post('/latexer', (req, res, next) => {
    const equation = req.body.equ;
     
    var opts = {
        'inline': true
    };
 
    tex2svg(equation, opts, clbk);
    function clbk(error, svg) {
        if (error) {
            throw error;
        }
        res.status(200).send({ svg });
    }
});

var server = app.listen(3000, function () {
    console.log("app running on port.", server.address().port);
});
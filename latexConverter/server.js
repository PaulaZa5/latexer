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

    // tex2svg(equation, opts, clbk);
    // function clbk(error, svg) {
    //     if (error) {
    //         throw error;
    //     }
    //     res.status(200).send({ svg });
    // }
    mjpage.mjpage('$y = mx + b$', {
        format: ["TeX"],
        output: 'svg',
        singleDollars: true, // allow single-dollar delimiter for inline TeX
        fragment: true, // return body.innerHTML instead of full document
        cssInline: true,  // determines whether inline css should be added
        displayMessages: false, // determines whether Message.Set() calls are logged
        displayErrors: false, // determines whether error messages are shown on the console
        undefinedCharError: false, // determines whether unknown characters are saved in the error array
        extensions: '', // a convenience option to add MathJax extensions
        // fontURL: 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/fonts/HTML-CSS', // for webfont urls in the CSS for HTML output
        MathJax: {} // options MathJax configuration, see https://docs.mathjax.org

    }, {

            ex: 6, // ex-size in pixels
            width: 100, // width of math container (in ex) for linebreaking and tags
            useFontCache: true, // use <defs> and <use> in svg output?
            useGlobalCache: false, // use common <defs> for all equations?
            // state: mjstate, // track global state
            linebreaks: false, // do linebreaking?
            equationNumbers: "none", // or "AMS" or "all"
            math: "", // the math to typeset
            html: false, // generate HTML output?
            css: false, // generate CSS for HTML output?
            mml: false, // generate mml output?
            svg: true, // generate svg output?
            speakText: true, // add spoken annotations to output?
            timeout: 10 * 1000, // 10 second timeout before restarting MathJax

        }, function (output) {
            // output is your final result
            console.log(output);
            res.status(200).send({svg: output});
        })
});

var server = app.listen(3000, function () {
    console.log("app running on port.", server.address().port);
});
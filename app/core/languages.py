JAVA_LANG = "java"
PY_LANG = "python"
JS_LANG = "javascript"
JSON_LANG = "json"
GO_LANG = "go"

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.python import Python3Lexer
from pygments.lexers.go import GoLexer

highlighter = {
    JAVA_LANG: JavaLexer(),
    PY_LANG: Python3Lexer(),
    JS_LANG: JavascriptLexer(),
    JSON_LANG: JsonLexer(),
    GO_LANG: GoLexer()
}


def syntax_highlighter(generated_code, code_language):
    return highlight(generated_code, highlighter.get(code_language), HtmlFormatter())

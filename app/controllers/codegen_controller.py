from PyQt5.QtGui import QTextCursor
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.python import Python3Lexer

from app.core.languages import *
from app.themes.theme_provider import pyg_styles
from app.tools import tool_plugins

highlighter = {
    JAVA_LANG: JavaLexer(),
    PY_LANG: Python3Lexer()
}


class CodeGenController:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app

        self.selected_tool = None
        self.parent.txt_code.document().setDefaultStyleSheet(pyg_styles())

        # app events
        self.app.data.signals.tool_switched.connect(self.on_tool_switched)

        # ui events
        self.parent.cmb_languages.currentIndexChanged[str].connect(self.switch_codegen_language)
        self.parent.btn_copy_clipboard.pressed.connect(self.on_copy_clipboard)

    def on_tool_switched(self, new_tool_name):
        selected_tool = tool_plugins.get(new_tool_name)
        self.init_languages(selected_tool.tool)

    def on_copy_clipboard(self):
        self.parent.txt_code.selectAll()
        self.parent.txt_code.copy()

    def switch_codegen_language(self, new_language):
        if not new_language or not self.selected_tool:
            return

        generated_code = self.selected_tool.generate_code(new_language)
        syntax_highlighted_code = self.syntax_highlighter(generated_code, new_language)
        self.parent.txt_code.clear()
        self.parent.txt_code.appendHtml(syntax_highlighted_code)

        # Scroll to top
        txt_cursor: QTextCursor = self.parent.txt_code.textCursor()
        txt_cursor.movePosition(QTextCursor.Start)
        self.parent.txt_code.setTextCursor(txt_cursor)

    def syntax_highlighter(self, generated_code, code_language):
        return highlight(generated_code, highlighter.get(code_language), HtmlFormatter())

    def init_languages(self, tool):
        self.selected_tool = tool
        self.parent.cmb_languages.clear()
        for lang in tool.languages:
            self.parent.cmb_languages.addItem(lang)

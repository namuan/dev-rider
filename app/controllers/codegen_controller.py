import logging
from pathlib import Path

from PyQt5.QtGui import QTextCursor

from app.core.languages import PY_LANG, JAVA_LANG, GO_LANG, JS_LANG, syntax_highlighter
from app.themes.theme_provider import pyg_styles
from app.tools import tool_plugins

language_main_file = {
    JAVA_LANG: "Main.java",
    PY_LANG: "main.py",
    GO_LANG: "main.go",
    JS_LANG: "main.js"
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
        self.parent.cmb_languages.currentIndexChanged[str].connect(
            self.switch_codegen_language
        )
        self.parent.btn_copy_clipboard.pressed.connect(self.on_copy_clipboard)

    def on_tool_switched(self, new_tool_name):
        self.parent.txt_code.clear()

        selected_tool = tool_plugins.get(new_tool_name)
        self.init_languages(selected_tool.tool)

    def on_copy_clipboard(self):
        self.parent.txt_code.selectAll()
        self.parent.txt_code.copy()

    def switch_codegen_language(self, new_language):
        if not new_language or not self.selected_tool:
            return

        generated_code = self.load_code(self.selected_tool, new_language)
        syntax_highlighted_code = syntax_highlighter(generated_code, new_language)
        self.parent.txt_code.clear()
        self.parent.txt_code.appendHtml(syntax_highlighted_code)

        # Scroll to top
        txt_cursor: QTextCursor = self.parent.txt_code.textCursor()
        txt_cursor.movePosition(QTextCursor.Start)
        self.parent.txt_code.setTextCursor(txt_cursor)

    def init_languages(self, tool):
        self.selected_tool = tool
        self.parent.cmb_languages.clear()
        available_languages = self.available_languages(tool)
        for lang in available_languages:
            self.parent.cmb_languages.addItem(lang)

        if available_languages:
            self.parent.cmb_languages.setCurrentIndex(0)

    def available_languages(self, tool):
        tool_dir = self.tool_dir(tool)
        if not tool_dir.exists():
            logging.info(
                "Unable to find any languages in {}".format(tool_dir.absolute())
            )
            return []

        return [x.name for x in self.tool_dir(tool).iterdir() if x.is_dir()]

    def load_code(self, tool, language):
        tool_name = type(tool).__name__
        main_file = language_main_file.get(language)
        code_file: Path = self.tool_dir(tool).joinpath(language).joinpath(main_file)
        logging.info("Loading {}".format(code_file))
        if code_file.exists():
            return code_file.read_text(encoding="utf-8")
        else:
            return "Unable to find code for {} in {}".format(tool_name, language)

    def tool_dir(self, tool):
        norm_tool_name = type(tool).__name__.lower()
        return (
            Path(__file__)
            .parent.parent.parent.joinpath("codegen")
            .joinpath(norm_tool_name)
        )

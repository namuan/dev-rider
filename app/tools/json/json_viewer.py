import json

from PyQt5.QtGui import QTextCursor

from app.tools.tool_plugin import ToolPlugin
from app.views.json_viewer_widget import JsonViewerWidget


class JsonViewer(ToolPlugin):
    def __init__(self):
        super().__init__(name="Json Viewer/Formatter", widget_class=JsonViewerWidget)
        self.json_content = None

    def bind_events(self):
        # bind ui events
        self.view.btn_format_json.pressed.connect(self.on_format_json)
        self.view.btn_minify_json.pressed.connect(self.on_minify_json)
        self.view.txt_json.textChanged.connect(self.on_json_text_changed)
        self.view.chk_sort_keys.stateChanged.connect(self.on_format_json)
        self.view.val_indent_level.valueChanged.connect(self.on_format_json)

        if not self.json_content:
            self.view.lbl_json_valid.setText("")

    def on_json_text_changed(self):
        source = self.view.txt_json.toPlainText()
        res, is_valid = self._parse_json(source)
        if is_valid:
            self.json_content = res
            self.view.lbl_json_valid.setText("Valid")
        else:
            self.view.lbl_json_valid.setText("InValid JSON")

    def on_format_json(self):
        if self.json_content:
            sort_keys = self.view.chk_sort_keys.isChecked()
            indent_level = self.view.val_indent_level.value()
            formatted_json = self._format_json(
                self.json_content, sort_keys, indent_level
            )
            self._replace_text(formatted_json)

    def on_minify_json(self):
        source = self.view.txt_json.toPlainText()
        if source:
            minified_json = self._minify_json(self.json_content)
            self._replace_text(minified_json)

    def _replace_text(self, new_text):
        txt_cursor: QTextCursor = self.view.txt_json.textCursor()
        txt_cursor.select(QTextCursor.Document)
        txt_cursor.insertText(new_text)

    @staticmethod
    def _format_json(json_obj, sort_keys, indent_level):
        return json.dumps(json_obj, sort_keys=sort_keys, indent=indent_level)

    @staticmethod
    def _minify_json(json_obj):
        return json.dumps(json_obj, separators=(",", ":"))

    @staticmethod
    def _parse_json(raw_json):
        try:
            j = json.loads(raw_json)
            return j, True
        except Exception as e:
            return e, False


tool = JsonViewer()

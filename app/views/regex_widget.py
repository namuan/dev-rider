from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QTextCursor

from app.generated.RegexMatcherWidget_ui import Ui_RegexMatcherWidget
from app.views import open_file_dialog


class RegexMatcherWidget(QtWidgets.QWidget, Ui_RegexMatcherWidget):
    def __init__(self, parent=None):
        super(RegexMatcherWidget, self).__init__(parent)
        self.setupUi(self)

    def open_file(self):
        file_location, _ = open_file_dialog(
            self,
            "Select Text File",
            "."
        )
        if file_location:
            return Path(file_location).read_text(encoding="utf-8")

    def highlight_match(self, start, end):
        fmt = QTextCharFormat()
        fmt.setBackground(Qt.darkGreen)
        fmt.setForeground(Qt.white)

        curr_cursor: QTextCursor = self.txt_document.textCursor()
        curr_cursor.setPosition(start, QTextCursor.MoveAnchor)
        curr_cursor.setPosition(end, QTextCursor.KeepAnchor)
        curr_cursor.setCharFormat(fmt)

    def reset_highlights(self):
        curr_cursor: QTextCursor = self.txt_document.textCursor()
        curr_cursor.select(QTextCursor.Document)
        curr_cursor.setCharFormat(QTextCharFormat())
        self.txt_document.setFocus()

    def scroll_to_match(self, start, end):
        self.txt_document.setFocus()

        curr_cursor: QTextCursor = self.txt_document.textCursor()
        curr_cursor.setPosition(start, QTextCursor.MoveAnchor)
        curr_cursor.setPosition(end, QTextCursor.KeepAnchor)
        self.txt_document.moveCursor(QTextCursor.EndOfWord)

        self.txt_document.setTextCursor(curr_cursor)

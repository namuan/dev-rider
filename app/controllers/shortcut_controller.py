from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut


class ShortcutController:
    def __init__(self, parent_window, app):
        self.parent = parent_window
        self.app = app

    def init_items(self):
        short = QShortcut(QKeySequence("Ctrl+G"), self.parent)
        short.activated.connect(
            self.parent.toolbar_controller.focus_on_devtools_combo_box
        )

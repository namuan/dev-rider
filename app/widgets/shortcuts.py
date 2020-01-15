from PyQt5.QtGui import *
from PyQt5.QtWidgets import QShortcut


def shortcut_items(self):
    short = QShortcut(QKeySequence("Ctrl+G"), self)
    short.activated.connect(self.toolbar_controller.focus_on_devtools_combo_box)

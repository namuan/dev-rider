from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QIcon, QKeySequence
from PyQt5.QtWidgets import QToolBar, QComboBox, QWidgetAction, QWidget, QSizePolicy, QAction, QShortcut

from app.core.constants import TOOLS_COMBO_ROLE, DEVTOOLS_COMBO_NAME
from app.tools import tool_plugins


class ShortcutController:
    def __init__(self, parent_window, app):
        self.parent = parent_window
        self.app = app

    def init_items(self):
        short = QShortcut(QKeySequence("Ctrl+G"), self.parent)
        short.activated.connect(self.parent.toolbar_controller.focus_on_devtools_combo_box)

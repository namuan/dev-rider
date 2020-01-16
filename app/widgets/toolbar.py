from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from app.core.constants import DEVTOOLS_COMBO_NAME


def toolbar_items(self):
    self.toolbar.setObjectName("maintoolbar")
    self.addToolBar(Qt.TopToolBarArea, self.toolbar)
    self.toolbar.setMovable(False)

    self.toolbar.addSeparator()

    toolbar_ctx_list = QComboBox(self)
    toolbar_ctx_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
    toolbar_ctx_list.setDuplicatesEnabled(False)
    toolbar_ctx_list.setEditable(True)
    toolbar_ctx_list.currentIndexChanged[str].connect(
        lambda new_tool: self.toolbar_controller.on_toolbar_tool_changed(new_tool)
    )
    toolbar_ctx_list_action = QWidgetAction(self)
    toolbar_ctx_list_action.setText(DEVTOOLS_COMBO_NAME)
    toolbar_ctx_list_action.setDefaultWidget(toolbar_ctx_list)
    self.toolbar.addAction(toolbar_ctx_list_action)

    spacer = QWidget(self)
    spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.toolbar.addWidget(spacer)

    toolbar_configure_action = QAction(
        QIcon(":/images/configure-48.png"), "Settings", self
    )
    toolbar_configure_action.triggered.connect(lambda x: x)
    self.toolbar.addAction(toolbar_configure_action)

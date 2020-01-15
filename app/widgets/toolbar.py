from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def toolbar_items(self):
    self.toolbar.setObjectName("maintoolbar")
    self.addToolBar(Qt.TopToolBarArea, self.toolbar)
    self.toolbar.setMovable(False)

    toolbar_ctx_list = QComboBox(self)
    toolbar_ctx_list.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
    toolbar_ctx_list.setDuplicatesEnabled(False)
    toolbar_ctx_list.setEditable(True)
    toolbar_ctx_list.currentIndexChanged[str].connect(
        lambda new_tool: self.toolbar_controller.on_toolbar_tool_changed(new_tool)
    )
    toolbar_ctx_list_action = QWidgetAction(self)
    toolbar_ctx_list_action.setText("DevTools")
    toolbar_ctx_list_action.setDefaultWidget(toolbar_ctx_list)
    self.toolbar.addAction(toolbar_ctx_list_action)

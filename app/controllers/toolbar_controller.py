from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QToolBar,
    QComboBox,
    QWidgetAction,
    QWidget,
    QSizePolicy,
    QAction,
)

from app.core.constants import DEVTOOLS_COMBO_NAME
from app.tools import tool_plugins


class ToolbarController:
    def __init__(self, parent_window, app):
        self.parent = parent_window
        self.toolbar = QToolBar()
        self.app = app
        self.populating_tools = True

    def __get_combo_box(self, action_name) -> QComboBox:
        toolbar_actions = self.toolbar.actions()
        tags_list_action = next(
            act for act in toolbar_actions if act.text() == action_name
        )
        return tags_list_action.defaultWidget()

    def init(self):
        tools_combo = self.__get_combo_box(DEVTOOLS_COMBO_NAME)
        tools_combo.clear()
        for ek, ev in tool_plugins.items():
            tools_combo.addItem(ev.tool.name, ek)

        # To avoid creating any view while we are populating tools in the combo box
        self.populating_tools = False

        selected_tool = self.app.data.get_selected_tool()
        found = tools_combo.findData(selected_tool)
        tools_combo.setCurrentIndex(found if found > 0 else 0)
        # Manually triggering to render the view as the index is not changing
        if found <= 0:
            self.on_toolbar_tool_changed(selected_tool)

    def on_toolbar_tool_changed(self, _):
        if self.populating_tools:
            return

        tools_combo = self.__get_combo_box("DevTools")
        current_tool = tools_combo.currentData()
        self.app.data.update_selected_tool(current_tool)

    def focus_on_devtools_combo_box(self):
        tools_combo = self.__get_combo_box("DevTools")
        tools_combo.setFocus(True)
        tools_combo.showPopup()

    def init_items(self):
        self.toolbar.setObjectName("maintoolbar")
        self.parent.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setMovable(False)

        self.toolbar.addSeparator()

        toolbar_ctx_list = QComboBox(self.parent)
        toolbar_ctx_list.setDuplicatesEnabled(False)
        toolbar_ctx_list.setEditable(True)
        toolbar_ctx_list.currentIndexChanged[str].connect(
            lambda new_tool: self.on_toolbar_tool_changed(new_tool)
        )
        toolbar_ctx_list_action = QWidgetAction(self.parent)
        toolbar_ctx_list_action.setText(DEVTOOLS_COMBO_NAME)
        toolbar_ctx_list_action.setDefaultWidget(toolbar_ctx_list)
        self.toolbar.addAction(toolbar_ctx_list_action)

        spacer = QWidget(self.parent)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        toolbar_configure_action = QAction(
            QIcon(":/images/configure-48.png"), "Settings", self.parent
        )
        toolbar_configure_action.triggered.connect(
            self.parent.config_controller.show_dialog
        )
        self.toolbar.addAction(toolbar_configure_action)

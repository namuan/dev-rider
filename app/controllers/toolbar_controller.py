from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem

from app.core.constants import TOOLS_COMBO_ROLE, DEVTOOLS_COMBO_NAME
from app.tools import tool_plugins


class ToolbarController:
    def __init__(self, toolbar, parent_window):
        self.parent = parent_window
        self.toolbar = toolbar

    def __get_combo_box(self, action_name):
        toolbar_actions = self.toolbar.actions()
        tags_list_action = next(act for act in toolbar_actions if act.text() == action_name)
        return tags_list_action.defaultWidget()

    def init(self):
        tools_combo = self.__get_combo_box(DEVTOOLS_COMBO_NAME)
        tools_combo.clear()
        for ek, ev in tool_plugins.items():
            item: QStandardItem = QStandardItem()
            item.setData(ev.tool.name, Qt.DisplayRole)
            item.setData(ek, TOOLS_COMBO_ROLE)
            tools_combo.addItem(ev.tool.name, item)

    def on_toolbar_tool_changed(self, new_tool):
        tools_combo = self.__get_combo_box("DevTools")
        item: QStandardItem = tools_combo.currentData()
        if not item:
            return

        selected_name = item.data(TOOLS_COMBO_ROLE)
        selected_tool = tool_plugins.get(selected_name)
        self.switch_tool(selected_tool)

    def switch_tool(self, selected_tool):
        selected_widget_class = selected_tool.tool.widget_class
        selected_widget = selected_widget_class(self.parent.scrollAreaWidgetContents)
        self.parent.replace_widget(selected_widget)
        selected_tool.tool.init_view(selected_widget)

    def focus_on_devtools_combo_box(self):
        tools_combo = self.__get_combo_box("DevTools")
        tools_combo.setFocus(True)
        tools_combo.showPopup()

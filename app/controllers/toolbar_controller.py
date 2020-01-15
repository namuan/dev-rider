import logging

tools_list = [
    "URL Encoder",
    "URL Decoder",
    "URL Parser",
    "HTML Encoder",
    "HTML Decoder",
    "Base64 Encoder",
    "Base64 Decoder"
]


class ToolbarController:
    def __init__(self, parent_window, toolbar):
        self.parent = parent_window
        self.toolbar = toolbar

    def __get_combox_box(self, action_name):
        toolbar_actions = self.toolbar.actions()
        tags_list_action = next(act for act in toolbar_actions if act.text() == action_name)
        return tags_list_action.defaultWidget()

    def init(self):
        tools_combo = self.__get_combox_box("DevTools")
        tools_combo.clear()
        for tool in tools_list:
            tools_combo.addItem(tool)

    def on_toolbar_tool_changed(self, new_tool):
        logging.info("Dev tool changed to {}".format(new_tool))

    def focus_on_devtools_combo_box(self):
        tools_combo = self.__get_combox_box("DevTools")
        tools_combo.setFocus(True)
        tools_combo.showPopup()

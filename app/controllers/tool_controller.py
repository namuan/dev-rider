import logging

from app.tools import tool_plugins


class ToolController:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app

        # app events
        self.app.data.signals.tool_switched.connect(self.on_tool_switched)

    def on_tool_switched(self, currently_selected_tool):
        logging.info("Switching to new tool {}".format(currently_selected_tool))
        selected_tool = tool_plugins.get(currently_selected_tool)

        selected_widget_class = selected_tool.tool.widget_class
        selected_widget = selected_widget_class(self.parent.scrollAreaWidgetContents)

        self.parent.replace_widget(selected_widget)
        selected_tool.tool.init_view(selected_widget)

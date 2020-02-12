import mistune

from app.tools.tool_plugin import ToolPlugin
from app.views.markdown_viewer_widget import MarkdownViewerWidget


class MarkdownViewer(ToolPlugin):
    def __init__(self):
        super().__init__(name="Markdown Viewer", widget_class=MarkdownViewerWidget)

    def bind_events(self):
        self.view.btn_render_html.pressed.connect(self.on_render_html)
        self.view.btn_raw_html.pressed.connect(self.on_raw_html)

    def on_render_html(self):
        markdown_html = self.md_to_html(self.view.txt_source.toPlainText())
        self.view.txt_target.setHtml(markdown_html)

    def on_raw_html(self):
        markdown_html = self.md_to_html(self.view.txt_source.toPlainText())
        self.view.txt_target.clear()
        self.view.txt_target.setPlainText(markdown_html)

    @staticmethod
    def md_to_html(md):
        return mistune.markdown(md)


tool = MarkdownViewer()

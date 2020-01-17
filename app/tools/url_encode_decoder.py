from urllib import parse

from app.codegen.urlencoding_codegen import generator
from app.tools.tool_plugin import ToolPlugin
from app.views.url_encoder_widget import UrlEncoderWidget


class UrlEncoderDecoder(ToolPlugin):
    def __init__(self):
        super().__init__(
            name="URL Encoder/Decoder",
            widget_class=UrlEncoderWidget,
            code_generator=generator,
        )

    def bind_events(self):
        # bind ui events
        self.view.btn_url_encode.pressed.connect(self.on_url_encode)
        self.view.btn_url_decode.pressed.connect(self.on_url_decode)

    def on_url_encode(self):
        source = self.view.txt_source.toPlainText()
        self.view.txt_target.setPlainText(parse.quote_plus(source))

    def on_url_decode(self):
        source = self.view.txt_source.toPlainText()
        self.view.txt_target.setPlainText(parse.unquote_plus(source))


tool = UrlEncoderDecoder()

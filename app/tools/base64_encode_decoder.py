import base64

from app.core.str_utils import str_to_bytes, bytes_to_str, plain_to_b64_str, b64_to_plain_str
from app.tools.tool_plugin import ToolPlugin
from app.views.base64_encoder_widget import Base64EncoderWidget


class Base64EncoderDecoder(ToolPlugin):
    def __init__(self):
        super().__init__(
            name="Base64 Encoder/Decoder", widget_class=Base64EncoderWidget
        )

    def bind_events(self):
        # bind ui events
        self.view.btn_b64_encode.pressed.connect(self.on_b64_encode)
        self.view.btn_b64_decode.pressed.connect(self.on_b64_decode)

    def on_b64_encode(self):
        source = self.view.txt_source.toPlainText()
        if source:
            self.view.txt_target.setPlainText(plain_to_b64_str(source))

    def on_b64_decode(self):
        source = self.view.txt_source.toPlainText()
        if source:
            self.view.txt_target.setPlainText(b64_to_plain_str(source))


tool = Base64EncoderDecoder()

import base64

from app.core.str_utils import str_to_bytes, bytes_to_str
from app.tools.ToolPlugin import ToolPlugin
from app.views.Base64EncoderWidget import Base64EncoderWidget


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
            self.view.txt_target.setPlainText(
                bytes_to_str(base64.standard_b64encode(str_to_bytes(source)))
            )

    def on_b64_decode(self):
        source = self.view.txt_source.toPlainText()
        if source:
            self.view.txt_target.setPlainText(
                bytes_to_str(base64.standard_b64decode(str_to_bytes(source)))
            )


tool = Base64EncoderDecoder()

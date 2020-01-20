from . import url_encode_decoder, base64_encode_decoder
from .markdown import markdown_viewer

tool_plugins = {
    "url_encoder": url_encode_decoder,
    "base64_decoder": base64_encode_decoder,
    'markdown_viewer': markdown_viewer
}

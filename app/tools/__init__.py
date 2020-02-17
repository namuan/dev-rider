from . import url_encode_decoder, base64_encode_decoder
from .markdown import markdown_viewer
from .json import json_viewer
from .regex import regex_matcher

tool_plugins = {
    "url_encoder": url_encode_decoder,
    "base64_decoder": base64_encode_decoder,
    "markdown_viewer": markdown_viewer,
    "json_viewer": json_viewer,
    "regex_matcher": regex_matcher,
}

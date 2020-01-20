from urllib import parse


def encode(src):
    return parse.quote_plus(src)


def decode(src):
    return parse.unquote_plus(src)


def test_url_encoder_decoder():
    plain = "http://www.example.com/?a=$123"
    encoded = "http%3A%2F%2Fwww.example.com%2F%3Fa%3D%24123"

    assert encode(plain) == encoded
    assert decode(encoded) == plain

import base64


def encode(src):
    # Convert String to bytes
    src_in_bytes = bytes(src, encoding="utf-8")

    # Encoding bytes to Base64
    src_in_bytes_base64 = base64.standard_b64encode(src_in_bytes)

    # Converting bytes back to String
    return src_in_bytes_base64.decode(encoding="utf-8")


def decode(src):
    # Convert string to bytes as before
    src_in_bytes_base64 = bytes(src, encoding="utf-8")

    # Decoding bytes
    src_in_string_bytes = base64.standard_b64decode(src_in_bytes_base64)

    # Converting bytes to string
    return src_in_string_bytes.decode(encoding="utf-8")


def test_base64_encoder_decoder():
    plain = "Hello World"
    encoded = "SGVsbG8gV29ybGQ="

    assert encode(plain) == encoded
    assert decode(encoded) == plain

def str_to_bytes(input_str: str):
    return bytes(input_str, encoding="utf-8")


def bytes_to_str(input_bytes: bytes):
    return input_bytes.decode(encoding="utf-8")

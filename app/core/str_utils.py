def str_to_bytes(input_str: str):
    return bytes(input_str, encoding="utf-8")


def bytes_to_str(input_bytes: bytes):
    return input_bytes.decode(encoding="utf-8")


def str_to_int(int_str, default=0):
    if int_str and type(int_str) is str:
        return int(int_str)

    return default


def str_to_bool(bool_str):
    if type(bool_str) is bool:
        return bool_str
    return bool_str.lower() in ("yes", "true", "t", "1")

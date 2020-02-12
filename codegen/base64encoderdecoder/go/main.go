package main

import (
    "encoding/base64"
)

func Base64Encode(src string) (encoded string) {
    encoded = base64.StdEncoding.EncodeToString([]byte(src))
    return
}

func Base64Decode(src string) (decoded string) {
    decodedBytes, _ := base64.StdEncoding.DecodeString(src)
    decoded = string(decodedBytes)
    return
}

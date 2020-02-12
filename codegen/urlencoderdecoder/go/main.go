package main

import "net/url"

func UrlEncode(src string) (encoded string) {
    encoded = url.QueryEscape(src)
    return
}

func UrlDecode(src string) (decoded string) {
    decoded, _ = url.QueryUnescape(src)
    return
}
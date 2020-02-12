package main

import (
    "github.com/gomarkdown/markdown"
    "strings"
)

func MarkdownToHtml(rawMd string) (htmlString string) {
    htmlBytes := markdown.ToHTML([]byte(rawMd), nil, nil)
    htmlString = strings.TrimSpace(string(htmlBytes))
    return
}

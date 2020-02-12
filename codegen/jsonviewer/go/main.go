package main

import (
    "bytes"
    "encoding/json"
)

type JsonMessage struct {
    Name string
    Age  int
}

func FormatJson(rawJson string) (formattedJson string) {
    jsonBytes := []byte(rawJson)
    var out bytes.Buffer
    json.Indent(&out, jsonBytes, "", "    ")
    return out.String()
}

func MinifyJson(formattedJson string) (minifiedJson string) {
    var out bytes.Buffer
    json.Compact(&out, []byte(formattedJson))
    return out.String()
}

func LoadJson(rawJson string) (jsonMessage JsonMessage) {
    json.Unmarshal([]byte(rawJson), &jsonMessage)
    return
}

func MarshalJson(message JsonMessage) (rawJson string) {
    rawJsonBytes, _ := json.Marshal(message)
    rawJson = string(rawJsonBytes)
    return
}

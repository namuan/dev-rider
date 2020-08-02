/* Javascript has the btoa() and atob() for interconversion between Base64 and ASCII.
However it doesn't support other Unicode characters. A workaround from
https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/btoa
is used. */

/* Other references:
https://developer.mozilla.org/en-US/docs/Glossary/Base64
https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/atob
Browser support: https://www.caniuse.com/#feat=atob-btoa
Polyfill: https://github.com/davidchambers/Base64.js
*/

function toBinary(string) {
    const codeUnits = new Uint16Array(string.length);
    for (let i = 0; i < codeUnits.length; i++) {
        codeUnits[i] = string.charCodeAt(i);
    }
    return String.fromCharCode(...new Uint8Array(codeUnits.buffer));
}
function fromBinary(binary) {
    try {
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < bytes.length; i++) {
            bytes[i] = binary.charCodeAt(i);
        }
        return String.fromCharCode(...new Uint16Array(bytes.buffer));
    } catch (error) {
        // If the string doesn't have any other non-ASCII characters, then return the sames string.
        // A different way to check for non-ASCII chars in a binary string can be implemented.
        return binary;
    }
}

function encodeStringToBase64(str) {
    try {
        const encoded = btoa(str.toString());
        return encoded;
    } catch (error) {
        //If the string has non-ASCII characters, convert them to a binary string.
        if (error.name == "InvalidCharacterError") {
            const convertedStrToBinary = toBinary(str);
            const encodedStr = btoa(convertedStrToBinary);
            return encodedStr;
        }
    }
}

function decodeStringFromBase64(src) {
    try {
        const decoded = atob(src);
        const decodedOriginal = fromBinary(decoded);
        return decodedOriginal;
    } catch (error) {
        //Handle error
        throw error;
    }
}

function testBase64EncoderAndDecoder() {
    const rawASCII = "Hello World";
    const rawNonASCII = "☸☹☺☻☼☾☿";
    const rawMixed = "😎😎Cool😎😎";

    const encodedASCII = "SGVsbG8gV29ybGQ=";
    const encodedNonASCII = "OCY5JjomOyY8Jj4mPyY=";
    const encodedMixed = "PdgO3j3YDt5DAG8AbwBsAD3YDt492A7e";

    console.log(encodedASCII === encodeStringToBase64(rawASCII));
    console.log(encodedNonASCII === encodeStringToBase64(rawNonASCII));
    console.log(encodedMixed === encodeStringToBase64(rawMixed));
    console.log(rawASCII === decodeStringFromBase64(encodedASCII));
    console.log(rawNonASCII === decodeStringFromBase64(encodedNonASCII));
    console.log(rawMixed === decodeStringFromBase64(encodedMixed));
}

testBase64EncoderAndDecoder();
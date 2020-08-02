function testURLEncoderAndDecoder(params) {

    const plain = "http://www.example.com/?a=$123"
    const encoded = "http%3A%2F%2Fwww.example.com%2F%3Fa%3D%24123"

    const encodeByFunction = encodeURIComponent(plain)
    const decodeByFunction = decodeURIComponent(encoded);

    console.log(plain === decodeByFunction);
    console.log(encoded === encodeByFunction);
}

testURLEncoderAndDecoder();
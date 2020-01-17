from app.core.languages import JAVA_LANG, PY_LANG


def gen_java():
    return """// Java code to convert text to Base64    
    """


def gen_py():
    return """# Python code
import base64

# 1. Encoding string to base64 string
sample = "Hello World"

# Convert String to bytes
sampleInBytes = bytes(sample, encoding="utf-8")

# Encoding bytes to Base64
sampleInBase64InBytes = base64.standard_b64encode(sampleInBytes)

# Converting bytes back to String
sampleInBase64 = sampleInBase64InBytes.decode(encoding="utf-8")

# Print output
print("Plain: {} -> Base64: {}".format(sample, sampleInBase64))

# 2. Decoding base64 string 
base64String = "SGVsbG8gV29ybGQ="

# Convert string to bytes as before
sampleInBase64InBytes = bytes(base64String, encoding="utf-8")

# Decoding bytes
plainBytes = base64.standard_b64decode(sampleInBase64InBytes)

# Converting bytes to string
plainString = plainBytes.decode(encoding="utf-8")

# Print output
print("Base64: {} -> Plain: {}".format(base64String, plainString))    
    """


generator = {JAVA_LANG: gen_java, PY_LANG: gen_py}

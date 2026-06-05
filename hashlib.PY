#hashlib

import hashlib

text = "Hello Python"

result = hashlib.md5(text.encode())

print(result.hexdigest())
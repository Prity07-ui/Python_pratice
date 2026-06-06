#zipfile

import zipfile

with zipfile.ZipFile("sample.zip", "w") as zipf:
    zipf.write("test.txt")

print("ZIP File Created")
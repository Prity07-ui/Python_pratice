#socket

import socket

host = socket.gethostname()

print("Host Name:", host)
print("IP Address:", socket.gethostbyname(host))
import socket

host = ""
port = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(1)

while True:
    client, address = s.accept()
    print("connected from %s " % address)
    data = client.recv(4096)
    client.send(data)
    client.close()
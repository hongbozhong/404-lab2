import socket

host = ""
port = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))
s.listen(10)

while True:
    conn, address = s.accept()
    print("connected from %s " % str(address))
    data = conn.recv(4096)
    print(data.decode())
    conn.send(data)
    conn.close()
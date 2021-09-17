import socket

host = ""
target_host = "www.google.com"
port = 8080
buffer_size = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(10)

s.connect((target_host, 80))

while True:
    conn, address = s.accept()
    data = conn.recv(buffer_size)

    s.send(data)
    resp = s.recv(buffer_size)
    
    conn.send(resp)
    conn.close()
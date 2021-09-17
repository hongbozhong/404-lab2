import socket

host = "www.google.com"
port = 80


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
s.send(request.encode())
result = s.recv(4096)
while len(result) > 0:
    print(result)
    result = s.recv(4096)

s.close()   



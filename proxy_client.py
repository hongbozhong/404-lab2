import socket

host = "127.0.0.1"
data = "I am client"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(host)
s.send(data.encode())
s.close()
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1' 
port = 512

conn_tup = (host, port)

client_socket.connect(conn_tup)

data = client_socket.recv(1024).decode()
print(data)
username = input()
client_socket.send(username.encode())

data = client_socket.recv(1024).decode()
print(data)
password = input()
client_socket.send(password.encode())

data = client_socket.recv(1024).decode()
print(data)

client_socket.close()
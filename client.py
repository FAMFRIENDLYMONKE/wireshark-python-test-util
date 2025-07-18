import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1' 
port = 9999

# Connection to hostname on the port.
client_socket.connect((host, port))

# Receive initial prompt
data = client_socket.recv(1024).decode()
print(data)
username = input()
client_socket.send(username.encode())

data = client_socket.recv(1024).decode()
print(data)
password = input()
client_socket.send(password.encode())

# Receive final message
data = client_socket.recv(1024).decode()
print(data)

client_socket.close()
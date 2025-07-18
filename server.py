import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'  # Listen on all interfaces
port = 512

server_socket.bind((host, port))

server_socket.listen(5)

print(f"[*] Listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"[+] Connection from {addr}")

    client_socket.send(b"Enter username: ")
    username = client_socket.recv(1024).decode().strip()
    client_socket.send(b"Enter password: ")
    password = client_socket.recv(1024).decode().strip()

    print(f"[*] Received username: {username}, password: {password}")

    client_socket.send(b"Thank you for logging in.\n")
    client_socket.close()
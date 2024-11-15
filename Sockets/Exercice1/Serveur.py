import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)

conn, address = server_socket.accept()
print('Connexion du client au serveur')

message = conn.recv(1024).decode()
print(f"Client : {message}")

conn.close()
server_socket.close()
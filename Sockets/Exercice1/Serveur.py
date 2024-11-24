import socket

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1) # Serveur Ecoute

conn, address = server_socket.accept()
print('Connexion du client au serveur')

message = conn.recv(1024).decode() # Decode le message du client.
print(f"Client : {message}")

conn.close() # Déconnexion
server_socket.close()
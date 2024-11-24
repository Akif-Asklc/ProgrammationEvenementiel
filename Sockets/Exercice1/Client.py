import socket

host = '127.0.0.1'
port = 12345

client_socket = socket.socket()
client_socket.connect((host, port)) # Connexion à 127.0.0.1
print("Connexion au serveur.")
reply = "Bonjour"
client_socket.send(reply.encode()) # Encode le message

# Decoder le message
reply = client_socket.recv(1024).decode()

# Déconnexion
client_socket.close()
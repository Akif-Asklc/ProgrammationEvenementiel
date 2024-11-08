import socket

# Configuration de l'adresse et du port
host = '127.0.0.1'
port = 12345

# Création de la socket du serveur
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Serveur en écoute sur {host}:{port}")

while True:
    conn, address = server_socket.accept()
    print(f"Connexion établie avec {address}")
    
    while True:
        # Réception du message du client
        message = conn.recv(1024).decode()
        if not message:
            break

        print(f"Message reçu : {message}")

        # Vérification des messages spéciaux
        if message.lower() == "bye":
            print("Le client a demandé de se déconnecter.")
            conn.send("Déconnexion du client...".encode())
            break
        elif message.lower() == "arret":
            print("Le client a demandé l'arrêt du serveur.")
            conn.send("Arrêt du serveur...".encode())
            conn.close()
            server_socket.close()
            exit()

        # Envoi de la réponse au client
        reply = f"Message reçu : {message}"
        conn.send(reply.encode())

    conn.close()
    print("Client déconnecté.")


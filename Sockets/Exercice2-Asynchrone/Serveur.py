import socket

# Configuration de l'adresse et du port
host = '0.0.0.0' # Adresse du serveur (localhost)
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

        print(f"Message reçu : {message}")

        # Vérification des messages spéciaux
        # upper --> Mettre le mot en majuscule
        try:
            if message.upper() == "BYE":
                print("Le client a demandé de se déconnecter.")
                conn.send("Déconnexion du client...".encode())
                break

            elif message.upper() == "ARRET":
                print("Le client a demandé l'arrêt du serveur.")
                conn.send("Arrêt du serveur...".encode())
                conn.close()
                server_socket.close()
                exit()

        except KeyboardInterrupt:  # CTRL+C
            print("Programme arrêté par le serveur.")

        # Envoi de la réponse au client
        reply = f"Message envoyé au serveur : {message}"
        conn.send(reply.encode())

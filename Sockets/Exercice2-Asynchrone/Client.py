import socket

# Configuration de l'adresse et du port
host = '127.0.0.1'  # Adresse du serveur (localhost)
port = 12345

running = True

# Création de la socket du client
client_socket = socket.socket()
client_socket.connect((host, port))

while running: #Boucle qui exécutera nos commandes jusqu'a l'arrêt

    # Lecture de l'entrée utilisateur
    message = input("Entrez votre message (BYE pour quitter, ARRET pour arrêter le serveur) : ")
    # Message
    client_socket.send(message.encode())

    # Réception de la réponse du serveur
    reply = client_socket.recv(1024).decode()
    print(f"Réponse du serveur : {reply}")

    try:
        # Vérification des commandes spéciales
        if message.upper() == "BYE":
            print("Déconnexion du client.")
            client_socket.close()
            break

        elif message.upper() == "ARRET":
            print("Arrêt du serveur demandé par le client.")
            client_socket.close()
            break
    except KeyboardInterrupt: #CTRL+C
        print("Programme arrêté par le serveur.")

# Quand j'ai fini l'échange de message
client_socket.close() # COMMUUNICATION TERMINEE
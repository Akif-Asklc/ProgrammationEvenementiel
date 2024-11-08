import socket
from random import randing
# Configuration de l'adresse et du port
host = '127.0.0.1'  # Adresse du serveur (localhost)
port = 12345

while True:
    # Création de la socket du client
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # Lecture de l'entrée utilisateur
    message = input("Entrez votre message (BYE pour quitter, ARRET pour arrêter le serveur) : ")
    client_socket.send(message.encode())

    # Réception de la réponse du serveur
    reply = client_socket.recv(1024).decode()
    print(f"Réponse du serveur : {reply}")

    # Vérification des commandes spéciales
    if message.lower() == "BYE":
        print("Déconnexion du client.")
        client_socket.close()
        break
    elif message.lower() == "ARRET":
        print("Arrêt du serveur demandé par le client.")
        client_socket.close()
        break

    client_socket.close()

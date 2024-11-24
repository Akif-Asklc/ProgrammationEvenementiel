from threading import Thread
import socket

def Envoie(socket): # Fonction d'envoie de message
    while True:
        msg = input("Ton message : ") # Message
        msg = msg.encode("utf-8") # Encode
        socket.send(msg) # Envoie
def Reception(socket): # Fonction de réception
    while True:
        requete_serveur = socket.recv(500) # Réception
        requete_serveur = requete_serveur.decode('utf-8')
        print(f"Client : {requete_serveur}")

Host = "127.0.0.1"
Port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

envoi = Thread(target=Envoie,args=[socket])
recep = Thread(target=Reception,args=[socket])

envoi.start()
recep.start()
from threading import Thread
import socket

def Envoie(socket): # Fonction d'envoie de message
    while True:
        msg = input("Ton message : ") # Message
        msg = msg.encode("utf-8") # Encode
        socket.send(msg) # Envoie


Host = "127.0.0.1"
Port = 4200

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

envoi = Thread(target=Envoie,args=[socket])

envoi.start()
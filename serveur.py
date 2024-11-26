from threading import Thread
import socket

def Envoie(socket): # Fonction d'envoie de message
    while True:
        msg = input("Ton message : ") # Message
        msg = msg.encode("utf-8") # Encode
        socket.send(msg) # Envoie

def Reception(socket):
    while True:
        requete_client = socket.recv(500)
        requete_client = requete_client.decode()
        print(f"Client : {requete_client}")
        if not requete_client : # Si on pert la connexion
            print("CLOSE")
            break

Host = "127.0.0.1"
Port = 4200

#Création du socket
socket = socket.socket()

socket.bind((Host,Port))
socket.listen(1)

#Le script s'arrête jusqu'a une connection
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")

envoi = Thread(target=Envoie,args=[client])
recep = Thread(target=Reception,args=[client])

envoi.start()
recep.start()

recep.join()

client.close()
socket.close()
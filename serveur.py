from threading import Thread
import socket
import time
import sys

'''
Veuillez renter les arguments comme ceci :
          python3 serveur.py HOST PORT
Exemple : python3 serveur.py 127.0.0.1 3000
'''

def compteRebours(): # Cette fonction servira a émettre un temps de pause.
   for i in range(3):
        x = 3
        o = x - i
        print("Affiche de la sortie dans : ", o)
        time.sleep(1) # une sec

def Envoie(client):
    # Fonction pour envoyer des messages au client
    while True:
        try:
            msg = "" # Chaine de caractères vides sinon ça bug
            msg = msg.encode("utf-8")
            client.send(msg)
            break
        except (ConnectionResetError, BrokenPipeError):
            print("Connexion avec le client interrompue.")
            break

def Reception(client):
    # Fonction pour recevoir des messages du client
    while True:
        try:
            requete_client = client.recv(500)  # Réception de données
            if not requete_client:  # Si la connexion est perdue
                print("Aucun client connecté. En attente d'une connexion...")
                return
            start = time.perf_counter()
            requete_client = requete_client.decode('utf-8')  # Décodage des données
            socket_server.settimeout(3)
            compteRebours() 
            end = time.perf_counter()
            print(requete_client)  # Affichage des données reçues
            print(f"Le message {round(end - start, 5)} seconde(s) à s'établir avec le client.")
        except (ConnectionResetError, # ConnectionResetError : Tentative de lire ou d'écrire sur un socket réinitialisé
                BrokenPipeError): # BrokenPipeError : Tentative d'écrire sur un socket déjà fermé
            print("La connexion est schlass..")
            break
    #client.close() -- Ce truc change rien..
            

# Adresse et port du serveur
Host = sys.argv[1] # Source : ZesteàSavoir
Port = int(sys.argv[2])

# Création du socket serveur
socket_server = socket.socket()
socket_server.bind((Host, Port))  # Liaison à l'adresse et au port
socket_server.listen(1)  # Attente d'une connexion
running = True

print("Serveur en attente de connexion...")
while True:
            client, ip = socket_server.accept()  # Attend une connexion entrante et l'accepte
            print("Une connexion est en cours...")
            time.sleep(0.5) # Eviter les relance à outrance de connexion faite par l'homme dernière son pc (moi)
            print("Le client d'IP", ip, "s'est connecté")

            print("Test 1") # Test pour voir si tout les communications fonctionnent
            start = time.perf_counter() # début de la prise de temps

            # Création des threads pour l'envoi et la réception
            envoi = Thread(target=Envoie, args=[client])
            recep = Thread(target=Reception, args=[client])

            # Démarrage des threads
            envoi.start()
            recep.start()
            print("Test 2") # Fin des test
            
            end = time.perf_counter()
            print(f"La connexion a prit {round(end - start, 4)} seconde(s) à s'établir avec le client.")
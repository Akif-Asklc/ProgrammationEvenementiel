import sys
import time # pour l'attente entre les connexions et les déconnexions
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import socket
from threading import Thread
import subprocess
import os

def compteRebours():
   for i in range(3):
        x = 3
        o = x - i
        time.sleep(1)

def Envoie(socket, running):
    while running(): # Thread qui gère la boucle -- Merci S.O
        try:
            msg = msg.encode("utf-8")
            socket.send(msg)
        except:
            break

def EnvoieFichier(socket, running, file):
    try:
        msg = file
        msg = msg.encode("utf-8")
        socket.send(msg)
        print(file)
    except:
        print("Une erreur est survenue.")

def Reception(socket, running):
    while running():
        try:
            requete_serveur = socket.recv(500)
            if not requete_serveur:
                return
            requete_serveur = requete_serveur.decode('utf-8')
            print(f"Serveur : {requete_serveur}")
        except:
            break

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        # Création du socket
        global serveur, port
        serveur = "127.0.0.1"
        port = "4200"

        # Paramètres de base
        self.setWindowTitle("Le serveur de tchat") # Nom de la fenetre
        self.resize(400,200) # redimensionnement de la taille
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Connexion avec le serveur
        self.setCentralWidget(widget) # ligne qui sert a centralisé la variable widget sur le self

        self.label_serveur = QLabel("Serveur") # Label
        self.text_serveur = QLineEdit(serveur) # Button Text

        self.label_port = QLabel("Port")  # Label
        self.text_port = QLineEdit(port)  # Button Text

        self.demarrage = QPushButton("Connexion") # Button Démarrage
        self.demarrage.setStyleSheet("background-color:green; border-radius: 3px")
        self.arret = QPushButton("Déconnexion")

        self.label = QLabel('No file selected') # Mettre le fichier
        self.upload_button = QPushButton('Upload')
        self.upload_button.setDisabled(True)

        self.arret.setDisabled(True)
        self.affichage = QLabel("")  # Button affichage
        self.rebours = QLabel()  # Compte à rebours

        self.quit = QPushButton("Quitter")  # Button Quitter

        grid = QGridLayout() # Création d'une Layout
        widget.setLayout(grid) # Ajouter les composants au grid layout

        grid.addWidget(self.label_serveur,0,0) # Serveur
        grid.addWidget(self.text_serveur,0,1)  # Serveur

        grid.addWidget(self.label_port,1,0) # Port
        grid.addWidget(self.text_port,1,1) # Port


        grid.addWidget(self.demarrage,2,0)  # Bouton démarrage
        grid.addWidget(self.arret, 2,1)  # Bouton démarrage

        grid.addWidget(self.label, 3,0)
        grid.addWidget(self.upload_button, 3,1)

        grid.addWidget(self.affichage,4,0) # Affichage Message
        grid.addWidget(self.rebours, 5,0) # Une manière de faire..

        grid.addWidget(self.quit, 6,0)  # Bouton Quit
 
        self.demarrage.clicked.connect(self.fonction__demarrage) # Action OK
        self.arret.clicked.connect(self.fonction__arret)
        self.upload_button.clicked.connect(self.Televersement)
        self.quit.clicked.connect(self.actionQuit)  # Action Quit

    def fonction__demarrage(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Recréer le socket
            serveur = self.text_serveur.text()
            port = int(self.text_port.text())

            self.sock.connect((serveur, port))
            time.sleep(0.5)
            self.affichage.setText("Connexion au serveur réussie.")

            self.demarrage.setDisabled(True) # Trouver grâce à une vidéo Youtube -- Sers à rendre non accessible une fois connecté de reappuyer sur 'Connexion'
            self.demarrage.setStyleSheet("background-color:grey; border-radius: 3px")
            
            self.arret.setDisabled(False)
            self.arret.setStyleSheet("background-color:red; border-radius: 3px")

            self.upload_button.setDisabled(False)
            
            self.running = True # Juste une variable booléenne pour dire quand s'arreter aux threads

            self.envoi = Thread(target=Envoie, args=(self.sock, lambda: self.running)) # lambda --> permet aux threads d'évaluer dynamiquement tout changement de valeur.
            self.recep = Thread(target=Reception, args=(self.sock, lambda: self.running))
            
            self.envoi.start()
            self.recep.start()

        except ValueError:
            self.show_error("Veuillez entrer un nombre valide.")
        except Exception as e: # Il génèrera l'erreur précisément et la représentera dans 'e'
            self.show_error(f"Erreur : {str(e)}")

    def fonction__arret(self):
        self.affichage.setText("Déconnexion en cours...")
        self.running = False # Arrêt de la boucle dans le thread.
        self.sock.close() # Déconnexion du client
        # time.sleep(2) -- Mauvaise idée :(
        self.affichage.setText("Vous êtes déconnecté du serveur.")
        self.arret.setDisabled(True)
        self.arret.setStyleSheet("background-color:grey; border-radius: 3px")
        self.demarrage.setDisabled(False)
        self.demarrage.setStyleSheet("background-color:green; border-radius: 3px")
        self.upload_button.setDisabled(True)

    def actionQuit(self):
        self.sock.close() # Pour éviter un bug car si on éteint en étant co, ça crash :(
        QCoreApplication.exit(0)
    
    def Televersement(self): # Aperçu de la fonction sur freeCodeCamp
        # Ouvrir un fichier et autoriser l'utilisateur a y accéder 
        options = QFileDialog.Options()
        options = QFileDialog.ReadOnly # L'autoriser seulement la lecture
        filename, _ = QFileDialog.getOpenFileName(self, "Sélectionnez un fichier .txt ", options=options)
        
        if filename:
            # Changement du label pour indiquer à l'utilisateur
            self.label.setText(filename.split('/')[5])
            # Enreigistrer le fichier txt (le fichier changera de nom aussi lors de l'envoi (fichier.txt) )
            try:
                with open(filename, 'r') as file: # le 'with' servira a fermer le fichier sans qu'on le demande
                    contenu = file.name # Merci StackOverflow du tuyau -- Prends le nom du fichier pour que je puisse l'appliquer après une commande -- python3 'contenu'
                    self.rebours.setText("")
                    # Vérifier l'extension du fichier 
                    extensionDuFichier = os.path.splitext(contenu)[1] 

                    # Exécute le fichier mis par l'utilisateur
                    if extensionDuFichier == '.py':
                        # Fonction subprocess() trouvé grâce à Chat GPT
                        resultat = subprocess.run(
                            ['python3', contenu],  # Commande pour exécuter le fichier
                            capture_output=True,  # Capture la sortie
                            text=True   # Garde la sortie en format texte
                        )
                        final = resultat.stdout.strip() # Prends le résultat de la sortie
                    elif extensionDuFichier == '.txt':
                        final = file.read()
                    elif extensionDuFichier == '.c':

                        # Un peu fait à l'arrache mais en gros on compile le fichier avec 'gcc' et on l'exécute
                        resultat = subprocess.run(
                            ['gcc', contenu],  # Commande pour exécuter le fichier
                            capture_output=True,  # Capture la sortie
                            text=True   # Garde la sortie en format texte
                        )
                        # celui-ci va nous créer un fichier qui s'appelle a.out et puis on va l'exécuter 
                        resultat = subprocess.run(
                            ['./a.out'],  # Commande pour exécuter le fichier
                            capture_output=True,  # Capture la sortie
                            text=True   # Garde la sortie en format texte
                        )
                        final = resultat.stdout.strip() # Prends le résultat de la sortie
                    else: # Le serveur n'acceptera pas les autres extensions
                        self.affichage.setText("Vous avez été éjecté du serveur par le serveur. \nVeuillez mettre uniquement les extensions suivantes : \n- .txt \n- .py \n- .c ")
                        self.running = False
                        self.arret.setDisabled(True)
                        self.arret.setStyleSheet("background-color:grey; border-radius: 3px")
                        self.demarrage.setDisabled(False)
                        self.demarrage.setStyleSheet("background-color:green; border-radius: 3px")
                        self.sock.close()
                    start = time.perf_counter() # début de la prise de temps
                    self.envoi = Thread(target=EnvoieFichier, args=(self.sock, lambda: self.running, final)) # lambda --> permet aux threads d'évaluer dynamiquement tout changement de valeur.
                    self.envoi.start()
                    self.sock.setblocking(1) # fonction trouvé sur StudyTonight -- Nous pouvons appeler setblocking(1) pour bloquer l'envoi et mettre le compte à rebours en place et setblocking(0) pour le débloquer
                    end = time.perf_counter() # début de la prise de temps
                    message = final
                    resultat = round(end - start, 3)
                    self.sock.setblocking(0)
                    self.rebours.setText(f"Le programme a mis : {resultat} secondes et a envoyé comme message : \n {message}.")

                # info
                QMessageBox.information(self, 'Envoi réussi !', 'Le fichier a bien été envoyé !')
            except Exception as e: # Il génèrera l'erreur précisément et la représentera dans 'e'
                self.show_error(f"Erreur : {str(e)}")

    def show_error(self, message): # Fonction en cas de pb
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Erreur")
        error_dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # Execution de la fenetre
    app.exec()
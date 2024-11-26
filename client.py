import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import socket
from threading import Thread


def Reception(client): # Fonction qui réceptionne les messages
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode()
        print(f"Client : {requete_client}")
        if not requete_client : # Si on pert la connexion
            print("CLOSE")
            break

def Envoie(socket): # Fonction qui envoie les messages
    while True:
        msg = input("Ton message : ") # Message
        msg = msg.encode("utf-8") # Encode
        socket.send(msg) # Envoie

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        # Création du socket
        global serveur, port
        serveur = "127.0.0.1"
        port = "4200"

        self.setCentralWidget(widget) # ligne qui sert a centralisé la variable widget sur le self

        self.label_serveur = QLabel("Serveur") # Label
        self.text_serveur = QLineEdit(serveur) # Button Text

        self.label_port = QLabel("Port")  # Label
        self.text_port = QLineEdit(port)  # Button Text

        self.demarrage = QPushButton("Connexion") # Button Démarrage
        self.arret = QPushButton("Arret")

        self.affichage = QLabel()  # Button affichage

        self.quit = QPushButton("Quitter")  # Button Quitter

        grid = QGridLayout() # Création d'une Layout
        widget.setLayout(grid) # Ajouter les composants au grid layout

        grid.addWidget(self.label_serveur,0,0) # Serveur
        grid.addWidget(self.text_serveur,0,1)  # Serveur

        grid.addWidget(self.label_port,1,0) # Port
        grid.addWidget(self.text_port,1,1) # Port


        grid.addWidget(self.demarrage,3,0)  # Bouton démarrage
        grid.addWidget(self.demarrage, 3, 1)  # Bouton démarrage

        grid.addWidget(self.affichage,4,0) # Affichage Message

        grid.addWidget(self.quit,5,0)  # Bouton Quit

        self.demarrage.clicked.connect(self.fonction__demarrage) # Action OK
        self.arret.clicked.connect(self.fonction__arret)
        self.quit.clicked.connect(self.actionQuit)  # Action Quit

        self.setWindowTitle("Le serveur de tchat") #Nom de la fenetre
        self.resize(300,200) # redimensionnement de la taille
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def fonction__demarrage(self):
        try:
            serveur = self.text_serveur.text()
            port = int(self.text_port.text())
            self.sock.connect((serveur, port))  # Connecte le socket au serveur

            self.affichage.setText("Connexion au serveur réussie.")  # Mise à jour du label d'affichage

            recep = Thread(target=Reception, args=[self.sock]) # Réception Message
            envoie = Thread(target=Envoie, args=[self.sock])  # Réception Message

            envoie.start()
            recep.start()

            recep.join()
            envoie.join()

            self.sock.close()
        except ValueError:
            self.show_error("Veuillez entrer un nombre valide.")

    def fonction__arret(self):
        pass

    def actionQuit(self):
        QCoreApplication.exit(0)

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
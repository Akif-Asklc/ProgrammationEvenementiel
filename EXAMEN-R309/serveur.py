import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import socket
from threading import Thread

# Bonjour, mon code se plante au moment ou je clique sur 'Démarrage du serveur'

socket = socket.socket()

def Reception(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode()
        print(f"Client : {requete_client}")
        if not requete_client : # Si on pert la connexion
            print("CLOSE")
            break

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        # Création du socket
        global serveur, port, clients
        serveur = "127.0.0.1"
        port = "4200"
        clients = "5"

        self.setCentralWidget(widget) # ligne qui sert a centralisé la variable widget sur le self

        self.label_serveur = QLabel("Serveur") # Label
        self.text_serveur = QLineEdit(serveur) # Button Text

        self.label_port = QLabel("Port")  # Label
        self.text_port = QLineEdit(port)  # Button Text

        self.label_nbClients = QLabel("Nombre de clients maximum ")  # Label
        self.text_nbClients = QLineEdit(clients)  # Button Text

        self.demarrage_arret = QPushButton("Démarrage du serveur") # Button Démarrage

        self.affichage = QLabel()  # Button affichage

        self.quit = QPushButton("Quitter")  # Button Quitter

        grid = QGridLayout() # Création d'une Layout
        widget.setLayout(grid) # Ajouter les composants au grid layout

        grid.addWidget(self.label_serveur,0,0) # Serveur
        grid.addWidget(self.text_serveur,0,1)  # Serveur

        grid.addWidget(self.label_port,1,0) # Port
        grid.addWidget(self.text_port,1,1) # Port

        grid.addWidget(self.label_nbClients,2,0) # Clients
        grid.addWidget(self.text_nbClients,2,1) # Clients


        grid.addWidget(self.demarrage_arret,3,0)  # Bouton démarrage

        grid.addWidget(self.affichage,4,0) # Affichage Message

        grid.addWidget(self.quit,5,0)  # Bouton Quit

        self.demarrage_arret.clicked.connect(self.fonction__demarrage) # Action OK
        self.quit.clicked.connect(self.actionQuit)  # Action Quit

        self.setWindowTitle("Le serveur de tchat") #Nom de la fenetre
        self.resize(300,200) # redimensionnement de la taille

    def fonction__demarrage(self):
        try:
            self.demarrage_arret = QPushButton("Arrêt du serveur")
            serveur = self.text_serveur
            port = self.text_port
            clients = self.text_nbClients

            socket.bind((serveur, port))
            socket.listen(1)

            client, ip = socket.accept() # Connexion établie entre serveur et clients
            self.affichage = QLabel(f"Le client d'ip, {ip}, s'est connecté")

            recep = Thread(target=Reception, args=[client]) # Réception Message
            recep.start()
            recep.join()

            client.close()
            socket.close()
        except ValueError:
            self.show_error("Veuillez entrer un nombre valide.")

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
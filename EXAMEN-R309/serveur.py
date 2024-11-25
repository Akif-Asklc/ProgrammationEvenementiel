import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget) # ligne qui sert a centralisé la variable widget sur le self

        self.label_serveur = QLabel("Serveur") # Label
        self.text_serveur = QLineEdit("") # Button Text

        self.label_port = QLabel("Port ")  # Label
        self.text_port = QLineEdit("")  # Button Text

        self.label_nbClients = QLabel("Nombre de clients maximum ")  # Label
        self.text_nbClients = QLineEdit("")  # Button Text

        self.demarrage_arret = QPushButton("Démarrage du serveur") # Button Démarrage

        self.affichage = QLabel("")  # Button affichage

        self.quit = QPushButton("Quitter")  # Button Quitter

        grid = QVBoxLayout() # Création d'une Layout
        widget.setLayout(grid) # Ajouter les composants au grid layout

        grid.addWidget(self.label_serveur) # Serveur
        grid.addWidget(self.text_serveur)  # Serveur

        grid.addWidget(self.label_port) # Port
        grid.addWidget(self.text_port) # Port

        grid.addWidget(self.label_nbClients) # Clients
        grid.addWidget(self.text_nbClients) # Clients

        grid.addWidget(self.demarrage_arret)  # Bouton démarrage

        grid.addWidget(self.affichage) # Affichage Message

        grid.addWidget(self.quit)  # Bouton Quit

        self.demarrage_arret.clicked.connect(self.__actionDemarrageArret) # Action OK
        self.quit.clicked.connect(self.__actionQuit)  # Action Quit

        self.setWindowTitle("Une première fenêtre") #Nom de la fenetre
        self.resize(300,200) # redimensionnement de la taille

    def __actionDemarrageArret(self):
        if self.demarrage_arret:
            self.demarrage_arret = QPushButton("Arrêt du serveur")  # Button Démarrage
    def __actionQuit(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # Execution de la fenetre
    app.exec()
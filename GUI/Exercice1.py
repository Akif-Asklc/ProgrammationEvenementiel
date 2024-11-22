import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget) # ligne qui sert a centralisé la variable widget sur le self

        self.lab = QLabel("Saissisez votre nom") # Label
        self.text = QLineEdit("") # Button Text
        self.affichage = QLabel("")  # Label
        self.ok = QPushButton("OK") # Button OK
        self.quit = QPushButton("Quit")  # Button OK

        grid = QGridLayout() # Création d'une Layout
        widget.setLayout(grid) # Ajouter les composants au grid layout

        grid.addWidget(self.lab, 0,0 ) # Label
        grid.addWidget(self.text, 1, 0)  # Label
        grid.addWidget(self.affichage, 2, 0)
        grid.addWidget(self.ok, 3, 0) #Bouton OK
        grid.addWidget(self.quit, 3, 1)  # Bouton Quit

        self.ok.clicked.connect(self.__actionOk) # Action OK
        self.quit.clicked.connect(self.__actionQuit)  # Action Quit

        self.setWindowTitle("Une première fenêtre") #Nom de la fenetre
        self.resize(300,200) # redimensionnement de la taille

    def __actionOk(self):
        prenom = self.text.text()
        self.affichage.setText(f"Bonjour {prenom}") # Affichage avec setText
    def __actionQuit(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # Execution de la fenetre
    app.exec()
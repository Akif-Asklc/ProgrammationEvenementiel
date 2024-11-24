import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget) # ligne qui sert a centralisé la variable widget sur le self

        self.temperature = QLabel("Température : ")
        self.text = QLineEdit("") # Button Text
        self.choix_unites = QLabel()  # Label pour affiché l'unité de mesure

        self.unites = QComboBox() # QComboBox sert à choisir entre K ou °C
        self.unites.addItems(["Celsius --> Kelvin", "Kelvin --> Celsius"])

        self.convertir = QPushButton("Convertir") # Button convertir

        self.resultat = QLabel()

        self.aide = QPushButton("?")  # Button OK

        grid = QGridLayout() # Création d'une Layout
        widget.setLayout(grid) # Ajouter les composants au grid layout

        grid.addWidget(self.temperature, 0, 1) # Label
        grid.addWidget(self.text, 0, 2)  # Label
        grid.addWidget(self.choix_unites, 0, 3)
        grid.addWidget(self.convertir, 1, 0) #Bouton convertir
        grid.addWidget(self.unites, 1, 1)  # Table
        grid.addWidget(self.resultat, 2,0) # Résultat
        grid.addWidget(self.aide, 3, 3)  # Bouton Aide


        self.convertir.clicked.connect(self.__actionConvertir) # Action OK
        self.aide.clicked.connect(self.__actionQuit)  # Action Quit

        self.setWindowTitle("Une première fenêtre") #Nom de la fenetre
        self.resize(350,200) # redimensionnement de la taille

    def __actionConvertir(self):
        # Il faut récupérer la valeur qu'on a entrer
        valeur_temperature = float(self.text.text()) # Float --> Mettre le texte en valeur décimale

        try:
            if self.unites.currentTextChanged() == "Celsius --> Kelvin":  # Ici, CurrentText va chercher à savoir ? se trouve dans 'unites
                self.choix_unites.setText("°C")  # Entrer °C
                if valeur_temperature < -273.15:
                    self.show_error("La température en Celsius ne peut pas être inférieure à -273,15K")
                    return
                    resultat = valeur_temperature + 273.15
                    unites = "K"
            elif self.unites.currentTextChanged() == "Kelvin --> Celsius":
                self.choix_unites.setText("K")

        except ValueError:
            raise "Il y a eu une erreur dans votre saisie."
    def __actionQuit(self):
        QCoreApplication.exit(0)

    # Fonction qui affichera les erreurs
    def erreur(self, message):
        erreur = QMessageBox()
        erreur.setIcon(QMessageBox.Warning)
        erreur.setText(message)
        erreur.setWindowTitle("Erreur")
        erreur.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() # Execution de la fenetre
    app.exec()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

app = QApplication(sys.argv) # Gère l’initialisation d’une application graphique
root = QWidget() # Support de la partie graphique
grid = QHBoxLayout() #
root.setLayout(grid)

root.resize(250, 250) # Taille en Lxl
root.setWindowTitle("Hello world!") # Titre de l'interface graphique
root.show() # Affichage


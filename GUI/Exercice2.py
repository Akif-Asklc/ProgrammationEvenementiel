import sys
from PyQt5.QtWidgets import *

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Conversion de Température")
        self.resize(350, 200)

        # Widgets
        self.label_temp = QLabel("Température :")
        self.input_temp = QLineEdit()
        self.label_unit = QLabel("°C")  # Par défaut Celsius

        self.convert_button = QPushButton("Convertir")
        self.combo_units = QComboBox()
        self.combo_units.addItems(["°C → K", "K → °C"])

        self.label_result_text = QLabel("Conversion :")
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)
        self.label_result_unit = QLabel("K")  # Par défaut Kelvin

        self.help = QPushButton("?")

        # Layout principal (GridLayout pour aligner les éléments)
        layout = QGridLayout()

        # Ligne 1 : Température d'entrée
        layout.addWidget(self.label_temp, 0, 0)
        layout.addWidget(self.input_temp, 0, 1)
        layout.addWidget(self.label_unit, 0, 2)

        # Ligne 2 : Bouton Convertir et combobox
        layout.addWidget(self.convert_button, 1, 1)
        layout.addWidget(self.combo_units, 1, 2)

        # Ligne 3 : Résultat de la conversion
        layout.addWidget(self.label_result_text, 2, 0)
        layout.addWidget(self.result_output, 2, 1)
        layout.addWidget(self.label_result_unit, 2, 2)

        # Ligne 4 : HELP
        layout.addWidget(self.help, 3,2)

        self.setLayout(layout)

        # Events
        self.combo_units.currentIndexChanged.connect(self.update_units)
        self.convert_button.clicked.connect(self.convert_temperature)
        # self.help.clicked.connect(self.show())

    def update_units(self):
        """Met à jour les unités en fonction de la sélection dans la combobox."""
        if self.combo_units.currentText() == "°C → K":
            self.label_unit.setText("°C")
            self.label_result_unit.setText("K")
        else:
            self.label_unit.setText("K")
            self.label_result_unit.setText("°C")

    def convert_temperature(self):
        try:
            # Récupérer la valeur entrée
            input_value = float(self.input_temp.text())

            # Conversion en fonction de l'unité choisie
            if self.combo_units.currentText() == "°C → K":
                if input_value < -273.15:
                    self.show_error("La température en Celsius ne peut pas être inférieure à -273,15.")
                    return
                result = input_value + 273.15
                unit = "°C"
            else:
                if input_value < 0:
                    self.show_error("La température en Kelvin ne peut pas être inférieure à 0.")
                    return
                result = input_value - 273.15
                unit = "K"

            # Afficher le résultat
            self.result_output.setText(f"{result:.2f} {unit}")
        except ValueError:
            self.show_error("Veuillez entrer un nombre valide.")

    def ouvrirFenetre(self):
        self.setWindowTitle("Conversion de Température")
        self.resize(200, 50)

    def show_error(self, message):
        """Affiche une boîte de dialogue en cas d'erreur."""
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setText(message)
        error_dialog.setWindowTitle("Erreur")
        error_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec_())

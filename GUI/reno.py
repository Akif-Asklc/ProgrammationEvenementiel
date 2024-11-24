import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QPushButton, QMessageBox
)

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Conversion Celsius ↔ Kelvin")
        self.resize(300, 200)

        # Widgets
        self.label_input = QLabel("Entrez la température :")
        self.input_temp = QLineEdit()
        self.unit_input = QLabel("")

        self.combo_units = QComboBox()
        self.combo_units.addItems(["Celsius → Kelvin", "Kelvin → Celsius"])

        self.convert_button = QPushButton("Convertir")
        self.result_label = QLabel("Résultat :")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_temp)
        layout.addWidget(self.unit_input)
        layout.addWidget(self.combo_units)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Events
        self.convert_button.clicked.connect(self.convert_temperature)

    def convert_temperature(self):
        try:
            # Récupérer la valeur entrée
            input_value = float(self.input_temp.text())

            # Conversion en fonction de l'unité choisie
            if self.combo_units.currentText() == "Celsius → Kelvin":
                self.unit_input = QLabel("K")
                if input_value < -273.15:
                    self.show_error("La température en Celsius ne peut pas être inférieure à -273,15.")
                    return
                result = input_value + 273.15
                unit = "K"

            else:
                if input_value < 0:
                    self.unit_input = "C"
                    self.show_error("La température en Kelvin ne peut pas être inférieure à 0.")
                    return
                result = input_value - 273.15
                unit = "°C"


            # Afficher le résultat avec l'unité
            self.result_label.setText(f"Résultat : {result:.2f} {unit}")
        except ValueError:
            self.show_error("Veuillez entrer un nombre valide.")

    def show_error(self, message):
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

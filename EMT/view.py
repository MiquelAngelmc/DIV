# Importar llibreríes 

from libraries import *

# Importar disseny emt

from emt import Ui_MainWindow

class EmtWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

    
    def stopHistory(self, buttonName, numName):
        button_obj = getattr(self, buttonName)
        button_obj.setText(numName)
    
    def update_scroll_labels(self, label_name, numStop, textStop, timeStop):

        label_obj = getattr(self, label_name)
        label_obj.setText(f"Parada {numStop}: {textStop} - {timeStop}")
    
    
    def display_warning(self, title: str, message: str):
        """Mostra un missatge d'advertència amb un títol i un missatge concrets."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Posa la icona d'advertència
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec() # Mostra la finestra i espera la interacció de l'usuari



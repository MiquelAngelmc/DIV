# Importar llibreríes 

from libraries import *

# Importar disseny emt

from emt import Ui_MainWindow

class EmtWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setup_scroll_area()


    def setup_scroll_area(self):
        """
        Configura el layout vertical que permetrà afegir elements dinàmics.
        
        ATENCIÓ: La funció setupUi ja ha creat self.scroll_layout.
        Si vols eliminar els elements estàtics (label_2 a label_7) per fer 
        espai, ho faries aquí.
        """
        # Creem un espaiador a la part inferior per assegurar-nos que els elements 
        # nous s'alineen a la part superior (start) i no al centre (default).
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.scroll_layout.addItem(spacer)
    
    def add_scroll_label(self, text: str):
        """
        Crea i afegeix un QLabel amb el text formatat al contenidor.
        """
        # Crear el nou Label
        new_label = QLabel(text) 
        
        # 1. Habilita l'ajust de text (Word Wrap) per a múltiples línies (CLAU)
        new_label.setWordWrap(True) 
        
        # 2. Habilita el mode RichText per als colors de línia
        new_label.setTextFormat(QtCore.Qt.TextFormat.RichText) 
        
        # Estil millorat per a la visualització
        new_label.setStyleSheet("""
            padding: 8px 10px; 
            border: 1px solid #1a73e8; 
            background-color: #f7f9fc; 
            color: #333333;
            border-radius: 5px;
            font-size: 10pt;
            line-height: 1.5;
        """)
        
        # 3. Alineació a dalt a l'esquerra (Això permet que el text llarg flueixi millor)
        new_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        
        # Inserim el label abans de l'últim element (l'espaiador)
        self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, new_label)

        
       
        self.scroll_layout.insertWidget(0, new_label)

    def stopHistory(self, buttonName, numName):
        button_obj = getattr(self, buttonName)
        button_obj.setText(numName)
    
    
    def display_warning(self, title: str, message: str):
        """Mostra un missatge d'advertència amb un títol i un missatge concrets."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)  # Posa la icona d'advertència
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec() # Mostra la finestra i espera la interacció de l'usuari



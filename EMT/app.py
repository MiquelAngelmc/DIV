# Importar classes

from model import EmtModel
from view import EmtWindow

#Importar llibreríes

from libraries import*

def main():
    """EMT main function."""
    app = QApplication([])

    view = EmtWindow()
    model = EmtModel(view)
    view.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
"""
Importar llibreries 

Sys serveix per interactuar amb amb l'entorn operatiu
PyQt6 permet crar interfícies gràfiques d'usuari(GUI)
"""

import sys

from PyQt6.QtWidgets import (
    QApplication,   #Classe principal
    QMainWindow,    #Finestra principal
    QLabel,         #Mostrar text o imatges
    QPushButton,    #Crear botons clicables
    QVBoxLayout,    #Posicionar elements en columna
    QWidget,        #Element base sobre el qual es construeix la finestra
    QLineEdit,      #Un camp d'entrada d'una sola línia que permet a l'usuari introduir text
    QGridLayout,    #Posicionar elements en una graella (molt útil per formularis o jocs)
    QHBoxLayout,    #Posicionar elements en fila
    QMessageBox,    # Missatge d'error
    QSpacerItem,    # Espaiador per layouts
    QSizePolicy    # Polítiques de mida per a widgets
)

from PyQt6 import QtCore, QtGui, QtWidgets

import requests
import json

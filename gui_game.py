from PyQt5 import QtWidgets,QtGui
import sys
from PyQt5.QtCore import Qt 

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFont(QtGui.QFont("Consolas", 12))
        QtWidgets.QMessageBox.information(self, "Welcome!", "Welcome to GUI Slots!")

app = QtWidgets.QApplication(sys.argv[1:])
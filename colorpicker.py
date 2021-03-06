from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.colorpicker = QColorDialog().exec_()

app = QApplication(sys.argv[1:])
win = ColorPicker()
sys.exit(app.exec_())
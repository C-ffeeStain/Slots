from PyQt5 import QtWidgets,QtGui,QtCore
import sys,random,time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
random.seed(time.time())
class Window(QMainWindow):
    money = 100
    cost = 25
    win = 75
    jackpot = 200
    def __init__(self):
        super().__init__()

        self.setGeometry(400,400,240,150)
        self.setStyleSheet("""QWidget{font-size: 12;}\nQMainWindow{background-color: rgb(60, 60, 60)}\n#money{color: lightgreen}""")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFont(QFont("Poppins.ttf", 12))
        self.center()

        self.title = QLabel("Casino Slots", self)
        self.title.setFont(QFont("Poppins.ttf", 13))
        self.title.setStyleSheet("QLabel{padding: 5 72 5 72; background-color: rgb(50, 50, 50)}")
        self.title.adjustSize()

        self.money_text = QLabel("$" + str(self.money), self)
        self.money_text.setObjectName("money")
        self.money_text.setFont(QFont("Poppins.ttf", 10))
        self.money_text.adjustSize()
        self.money_text.move(5,7)

        self.quit = QPushButton(self)
        self.quit.setText("Quit")
        self.quit.adjustSize()
        self.quit.move(165, 100)

        self.oldPos = self.pos()
        self.show()
        # QtWidgets.QMessageBox.information(self, "Welcome!", "Welcome to GUI Slots!")
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        

app = QtWidgets.QApplication(sys.argv[1:])
win = Window()
sys.exit(app.exec_())
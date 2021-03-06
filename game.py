import sys,random,time,json
from pathlib import Path
from time import sleep
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from datetime import datetime
from urllib.request import urlretrieve
random.seed(time.time())

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

class Window(QMainWindow):
    last_uid = 0
    money = 100
    cost = 25
    win = 75
    jackpot = 200
    
    def log(self, msg : str):
        self.report.setText(msg)
        with open("gamble.log", "a") as gl:
            gl.write(datetime.now().strftime("%m/%d %H:%M:%S") + ": " + msg + "\n")
    def roll(self):
        self.all_slot_nums = [[],[],[]]
        if self.money >= self.cost:
            self.money -= self.cost
        else:
            self.log("Aww... You don't have enough money.")
            return None
        self.money_text.setText("$" + str(self.money))
        for i in range(3):
            num = random.randint(1, 9)
            if i == 0:
                self.slot1.setText(str(num))
                self.slot1.adjustSize()
            elif i == 1:
                self.slot2.setText(str(num))
                self.slot2.adjustSize()
            else:
                self.slot3.setText(str(num))
                self.slot3.adjustSize()
            
            self.all_slot_nums[i].append(num) 
        if self.all_slot_nums[0][-1] == 7 and self.all_slot_nums[1][-1] == 7 and self.all_slot_nums[2][-1] == 7:
            self.money += self.jackpot
            self.log("Congratulations! You won the jackpot and got ${}.".format(self.jackpot))
            self.report.setStyleSheet("#report{color: gold}")
        elif all_equal([self.all_slot_nums[0][-1], self.all_slot_nums[1][-1], self.all_slot_nums[2][-1]]):
            self.money += self.win
            self.report.setStyleSheet("#report{color: green}")
            self.log("Yay! You won and got ${}.".format(self.win))
        else:
            self.log("Maybe next time... You lost and won nothing.")
            self.report.setStyleSheet("#report{color: maroon}")
        self.report.adjustSize()
    def __init__(self):
        urlretrieve("https://github.com/c-ffeestain/slots/raw/main/data.json", "data.json")
        with open("data.json") as jp:
            self.data = json.load(jp)
        self.jackpot = int(self.data["jackpot"])
        self.money = int(self.data["money"])
        
        print(self.jackpot)

        super().__init__()

        if not Path("gamble.log").exists():
            with open("gamble.log", "w") as gl:
                gl.write(datetime.now().strftime("%m/%d %H:%M:%S") + ": Created log file.\n")
        self.setGeometry(400,400,240,150)
        self.setStyleSheet("""
        QMainWindow{background-color: rgb(60, 60, 60)}
        QPushButton[flat="true"]{background-color: #575757;border: 5px;padding: 5px 20px 5px 20px;}
        #report{color:darkgray;}
        #money{color: lightgreen}""")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFont(QFont("Poppins.ttf", 12))
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.center()

        self.roll_timer = QTimer(self)
        self.roll_timer.setInterval(100)
        # self.roll_timer.timeout.connect()

        self.title = QLabel("Casino Slots", self)
        self.title.setFont(QFont("Poppins.ttf", 13))
        self.title.setStyleSheet("QLabel{padding: 5 72 5 72; background-color: rgb(50, 50, 50)}")
        self.title.adjustSize()

        self.report = QLabel("You haven't rolled the slots yet.", self)
        self.report.setObjectName("report")
        self.report.setFont(QFont("Poppins.ttf", 9))
        self.report.setAlignment(Qt.AlignCenter)
        self.report.adjustSize()
        self.report.move(10, 40)

        self.money_text = QLabel("$" + str(self.money), self)
        self.money_text.setObjectName("money")
        self.money_text.setFont(QFont("Poppins.ttf", 10))
        self.money_text.adjustSize()
        self.money_text.move(5,7)

        self.slot1 = QLabel("1", self)
        self.slot1.setFont(QFont("Poppins.ttf", 30))
        self.slot1.move(75, 50)
        self.slot1.adjustSize()

        self.slot2 = QLabel("2", self)
        self.slot2.setFont(QFont("Poppins.ttf", 30))
        self.slot2.move(105, 50)
        self.slot2.adjustSize()

        self.slot3 = QLabel("3", self)
        self.slot3.setFont(QFont("Poppins.ttf", 30))
        self.slot3.move(135, 50)
        self.slot3.adjustSize()

        self.roll_btn = QPushButton("Roll", self, flat=True)
        self.roll_btn.setFont(QFont("Poppins.ttf", 10))
        self.roll_btn.move(35, 110)
        self.roll_btn.adjustSize()
        self.roll_btn.clicked.connect(self.roll)

        self.quit = QPushButton("Quit", self, flat=True)
        self.quit.setFont(QFont("Poppins.ttf", 10))
        self.quit.adjustSize()
        self.quit.move(155, 110)
        self.quit.clicked.connect(sys.exit)

        self.oldPos = self.pos()
        self.show()
        # QMessageBox.information(self, "Welcome!", "Welcome to GUI Slots!")
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        

app = QApplication(sys.argv[1:])
win = Window()
sys.exit(app.exec_())
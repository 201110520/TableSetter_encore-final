
from PyQt5.QtCore import pyqtSignal
from POS import MainWindow
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("login.ui")[0]


class loginWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_Button.clicked.connect(self.login)
    
    def login(self):
        print("로그인")
        self.Mainwindow = MainWindow(self)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lw = loginWindow()
    lw.show()
    exit(app.exec_())
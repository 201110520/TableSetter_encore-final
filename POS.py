
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('POS.ui')
form_class = uic.loadUiType(form)[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.accContain.hide()
        self.tableContain.hide()
        self.menuContain.hide()
        self.qrContain.hide()
        self.table.clicked.connect(self.tableView)
        self.acc.clicked.connect(self.accView)
        self.menu.clicked.connect(self.menuView)
        self.qr.clicked.connect(self.qrView)

    def tableView(self):
        self.accContain.hide()
        self.menuContain.hide()
        self.qrContain.hide()
        self.tableContain.show()
        print("테이블 화면")
        self.table.setDisabled(True)
        self.acc.setDisabled(False)
        self.menu.setDisabled(False)
        self.qr.setDisabled(False)

    def accView(self):
        self.menuContain.hide()
        self.tableContain.hide()
        self.qrContain.hide()
        self.accContain.show()
        print("통계화면")
        self.acc.setDisabled(True)
        self.table.setDisabled(False)
        self.menu.setDisabled(False)
        self.qr.setDisabled(False)

    def menuView(self):
        self.accContain.hide()
        self.tableContain.hide()
        self.qrContain.hide()
        self.menuContain.show()
        print("메뉴화면")
        self.acc.setDisabled(False)
        self.table.setDisabled(False)
        self.menu.setDisabled(True)
        self.qr.setDisabled(False)

    def qrView(self):
        self.accContain.hide()
        self.tableContain.hide()
        self.menuContain.hide()
        self.qrContain.show()
        print("qr화면")
        self.acc.setDisabled(False)
        self.table.setDisabled(False)
        self.menu.setDisabled(False)
        self.qr.setDisabled(True)
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
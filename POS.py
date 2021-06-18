import sys
import os
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow , QDialog
from POSsql import LoginCtrl , AddUserCtrl, Menuctrl
from adduser import adduer_M
from CertificateStatus import CertificateStatus_M
from table import tableWidget
from menu import menuWidget
import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('POS.ui')
form_class = uic.loadUiType(form)[0]

form_class2 = uic.loadUiType("login.ui")[0]
loginCtrl = LoginCtrl()
adduserctrl = AddUserCtrl()
login_re = POSvariable

class MainWindow(QMainWindow, form_class):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.accContain.close()
        self.tableContain.close()
        self.menuContain.close()
        self.qrContain.close()
        self.table.clicked.connect(self.tableView)
        self.acc.clicked.connect(self.accView)
        self.menu.clicked.connect(self.menuView)
        self.qr.clicked.connect(self.qrView)
        self.actionstore_user_add.triggered.connect(self.storeUserAdd)
        self.actionGenerate_Certificate.triggered.connect(self.generateCertificate)
        self.adduserdialog = adduer_M(self)
        self.CertificateStatus = CertificateStatus_M(self)

    def storeUserAdd(self):
        self.adduserdialog.show()
    
    def generateCertificate(self):
        self.CertificateStatus.show()
        print("암호키 생성")

    def tableView(self):
        self.accContain.hide()
        self.menuContain.hide()
        self.qrContain.hide()
        tableWidget()
        self.tableContain.show()
        print("테이블 화면")
        self.table.setDisabled(True)
        self.acc.setDisabled(False)
        self.menu.setDisabled(False)
        self.qr.setDisabled(False)
        #threading.Timer(2.5, self.tableView()).start()

    def accView(self):
        self.menuContain.hide()
        self.tableContain.hide()
        self.qrContain.hide()
        self.accContain.show()
        print(self)
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
        menuWidget()
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
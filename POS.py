import sys
import os

import pymysql
import POSvariable
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow , QDialog
from POSsql import LoginCtrl , AddUserCtrl, Menuctrl
from adduser import adduer_M
from CertificateStatus import CertificateStatus_M
from table import tableWidget
from menu import menuWidget
from POSvariable import TABLE_NUM



import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('POS.ui')
form_class = uic.loadUiType(form)[0]


loginCtrl = LoginCtrl()
adduserctrl = AddUserCtrl()
login_re = POSvariable
#tablewidget1 = tableWidget()

class TestThread(QThread):
    # 쓰레드의 커스텀 이벤트
    # 데이터 전달 시 형을 명시해야 함
    threadEvent = QtCore.pyqtSignal(int)
    update = pyqtSignal(int)
    #tablewidget1 = tableWidget()
    def __init__(self, parent=None):
        super().__init__()
        self.n = 0
        self.main = parent
        self.isRun = False
 
    def run(self):
        while self.isRun:
            print('쓰레드 : ' + str(self.n),TABLE_NUM)

            # 'threadEvent' 이벤트 발생
            # 파라미터 전달 가능(객체도 가능)
            self.threadEvent.emit(self.n)
            self.update.emit(TABLE_NUM)
            #MainWindow()
            QApplication.processEvents()

            self.n += 1
            self.sleep(1)

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

        self.th = TestThread(self)
        # 쓰레드 이벤트 연결
        self.th.threadEvent.connect(self.threadEventHandler)
        self.th.update.connect(self.tabletotal)

    def storeUserAdd(self):
        self.adduserdialog.show()
    
    def generateCertificate(self):
        self.CertificateStatus.show()
        print("암호키 생성")

    @pyqtSlot(int)
    def threadEventHandler(self, n):
        print('메인 : threadEvent(self,' + str(n) + ')')
    @pyqtSlot(int)
    def tabletotal(self,x):
        tablewidget1 = tableWidget()
        print(x)
        tablewidget1.retranslateUi(x)
        #tablewidget1.refresh()
        self.tableContain.repaint()
        self.tableContain.show()
        QApplication.processEvents()
        #tablewidget1.close()
        #tablewidget1.close()
        #

    def tableView(self):
        self.accContain.close()
        self.menuContain.close()
        self.qrContain.close()
        tableWidget(tableWidget())
        self.tableContain.show()
        print("테이블 화면")
        self.table.setDisabled(True)
        self.acc.setDisabled(False)
        self.menu.setDisabled(False)
        self.qr.setDisabled(False)
        if not self.th.isRun:
            print('메인 : 쓰레드 시작')
            self.th.isRun =False #True
            self.th.start()
        #threading.Timer(2.5, tableWidget.totalinfo(tableWidget())).start()

    def accView(self):
        self.menuContain.close()
        self.tableContain.close()
        self.qrContain.close()
        self.accContain.show()
        print(self)
        print("통계화면")
        self.acc.setDisabled(True)
        self.table.setDisabled(False)
        self.menu.setDisabled(False)
        self.qr.setDisabled(False)
        if self.th.isRun:
            print('메인 : 쓰레드 정지')
            self.th.isRun = False

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
        if self.th.isRun:
            print('메인 : 쓰레드 정지')
            self.th.isRun = False

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
        if self.th.isRun:
            print('메인 : 쓰레드 정지')
            self.th.isRun = False
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
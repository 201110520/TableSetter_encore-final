import sys
import os
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QTabWidget,QPushButton,QLabel,QLineEdit, QDialog
from POSsql import Payctrl, Tablectrl



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('payment2.ui')
form_class2 = uic.loadUiType(form)[0]
payctrl = Payctrl()
tablectrl = Tablectrl()

class paymodul(QDialog,form_class2):
    total = 0
    paymon= 0
    ordernum = 0
    num =0
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.payBtn.clicked.connect(self.paidcard)
        self.payBtn_2.clicked.connect(self.paidcash)
        self.Pay.textChanged.connect(self.LeftMoney)
        self.Pay_2.textChanged.connect(self.LeftMoney)
        self.receivedMoney.textChanged.connect(self.ChangeMoney)
        #self.winhide()

    def LeftMoney(self):
        num = self.Pay.text()
        num = self.Pay_2.text()
        self.paymon = self.total-int(num)
        self.leftMoney.setText(str(self.paymon))
        self.leftMoney_2.setText(str(self.paymon))

    def ChangeMoney(self):
        pay = int(self.Pay_2.text())
        rece = int(self.receivedMoney.text())
        self.changedMoney.setText(str(rece-pay))

    def setting(self, tablenum):
        self.num = tablenum
        total1 , self.ordernum = payctrl.total(tablenum)
        self.total = total1
        self.totalPrice_2.setText(str(self.total))
        self.totalPrice.setText(str(self.total))
        print(tablenum)

    def paidcard(self):
        cardnum1 = self.cardNum1.text()
        cardnum2 = self.cardNum2.text()
        cardnum3 = self.cardNum3.text()
        cardnum4 = self.cardNum4.text()
        cardnum = '{0}{1}{2}{3}'.format(cardnum1,cardnum2,cardnum3,cardnum4)
        pay=self.Pay.text()
        payctrl.paidcard(self.ordernum,cardnum,pay)
        self.paymon = self.leftMoney.text()
        self.total = self.paymon
        self.paymon =0
        self.winhide(self.total)
        self.totalPrice_2.setText(self.total)
        self.totalPrice.setText(self.total)
        print('카드')
    
    def paidcash(self):
        pay = self.Pay_2.text()
        payctrl.paidcash(self.ordernum,pay)
        self.paymon = self.leftMoney_2.text()
        self.total = self.paymon
        self.paymon =0
        self.winhide(self.total)
        self.totalPrice_2.setText(self.total)
        self.totalPrice.setText(self.total)
        print('현금')
    
    def winhide(self,num):
        if int(num) <= 0:
            self.hide()
            tablectrl.payment(self.num)
        


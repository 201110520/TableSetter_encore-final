import sys
import os
from PyQt5 import uic
#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QPushButton, QApplication, QTableWidget, QTableWidgetItem, QWidget, QSpinBox
import POSvariable
from POSsql import Tablectrl
from payment import paymodul
tablectrl =  Tablectrl()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('table_info.ui')
form_class = uic.loadUiType(form)[0]




class tableInfoWidget(QDialog, form_class):
    menurow = 0 # menu창 row col
    menucol = 0
    billrow = 0 # 영수증화면 row col
    billcol = 0
    NUM = 0 #테이블번호
    billTablerow = 0
    billTablecard = 0
    billTablecash = 0
    addlist= []
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.orderDelete.clicked.connect(self.orderDeleteF)
        self.orderAdd.clicked.connect(self.orderAddFB)
        self.orderPayment.clicked.connect(self.orderPaymentF)
        self.windowExit.clicked.connect(self.windowExitF)
        #self.menuWidget.verticalHeader().setVisible(False)
        #self.billWidget.verticalHeader().setVisible(False)
        #self.stateWidget.verticalHeader().setVisible(False)
        self.menuWidget.cellClicked.connect(self.menucolsave)
        self.billWidget.cellClicked.connect(self.billrowsave)
        self.menuWidget.cellClicked.connect(self.orderAddF)
        self.billWidget.cellClicked.connect(self.orderDeleteF)
        self.payDialog = paymodul()
        #self.menuLoading()
        #self.billLoading()
        #self.orderAddF()
    
    def menucolsave(self, row, col):
        tableInfoWidget.menurow = row
        tableInfoWidget.menucol = col
        print(tableInfoWidget.menurow,tableInfoWidget.menucol)
    
    def billrowsave(self, row, col):
        tableInfoWidget.billrow = row
        tableInfoWidget.billcol = col
        print(tableInfoWidget.billrow,tableInfoWidget.billcol)
    

    def labeltext(self, text):
        tableInfoWidget.NUM=text
        self.tableNumLabel.setText(str(tableInfoWidget.NUM)+'번 테이블')
        
    def menuLoading(self):
        row = tablectrl.TableMenuLoad()
        count = len(row)
        self.menuWidget.setRowCount(count)
        for x in range(count):
            name, price, category = row[x]
            self.menuWidget.setItem(x,0,QTableWidgetItem(name))
            self.menuWidget.setItem(x,1,QTableWidgetItem(price))

    def isMenuOnTable(self, menu):
        count = self.billTablerow
        for i in range(count):
            if self.billWidget.item(i, 0) != None:
                # 메뉴 테이블 i번째 행에 적힌 메뉴가 menu 라면 몇번째 행인지 i를 return
                if self.billWidget.item(i, 0).text() == menu:
                    return i
        return False

    def HowManyOnMenuTable(self, row):
        return int(self.billWidget.item(row, 1).text()) 
        
    
    def billLoading(self):
        self.billWidget.clearContents()
        row=[]
        card =0
        cash = 0
        row, card, cash = tablectrl.billLoad(tableInfoWidget.NUM)
        self.billTablerow = len(row)
        self.billTablecard = card
        self.billTablecash = cash
        count = self.billTablerow
        self.billWidget.setRowCount(count)
        print(len(row),count)
        y=0
        name = ''
        price =''
        amount=0
        paycode = 0
        for x in range(0,count):
            name = ''
            price =''
            amount=0
            paycode = 0
            amount1 = 0
            name, price, amount, paycode = row[x]
            print(row[x])
            if type(self.isMenuOnTable(name)) == bool and self.isMenuOnTable(name) == False:
                self.billWidget.setItem(x-y,0,QTableWidgetItem(name))
                self.billWidget.setItem(x-y,1,QTableWidgetItem(str(amount)))
                self.billWidget.setItem(x-y,2,QTableWidgetItem(price))
                self.billWidget.setItem(x-y,3,QTableWidgetItem(str(int(price)*amount)))
                #print(name, price, amount,x,y)
            else:
                #count = self.billTablerow
                i = self.isMenuOnTable(name)
                
                amount1 = int(self.HowManyOnMenuTable(i))
                amount += amount1
                self.billWidget.setItem(i, 1, QTableWidgetItem(str(amount)))  # 수량
                self.billWidget.setItem(i,3,QTableWidgetItem(str(int(price)*amount)))  # 합계
                y += 1
                self.billWidget.setRowCount(count-1)
                #print(name, price, amount,amount1,i)
        
        print(card,cash)
        self.stateWidget.setRowCount(1)
        self.stateWidget.setItem(0,0,QTableWidgetItem(str(card)))
        self.stateWidget.setItem(0,1,QTableWidgetItem(str(cash)))
        self.stateWidget.setItem(0,2,QTableWidgetItem(str((card+cash)-card)))
        print('영수증로딩')
        return 0

    
    def orderDeleteF(self):
        print(self.NUM)
        row = self.billrow
        data = []
        for col in range(4):
            it = self.billWidget.item(row, col)
            text = it.text() if it is not None else ""
            data.append(text)
        print(data)
        #menuctrl.menuOpenClose(data)
        #self.billWidget.clearContents()
        #self.billLoading()
        print('주문삭제')

    def orderAddF(self):
        print(tableInfoWidget.NUM)
        row = tableInfoWidget.menurow
        data = []
        for col in range(2):
           it = self.menuWidget.item(row, col)
           text = it.text() if it is not None else ""
           data.append(text)
        #print(data)
        self.addlist.append(data[0])
        print(self.addlist)
        self.writeOnTable(data[0], data[1])
        
        print('주문 담기')

    def orderAddFB(self):
        #self.addlist.pop(0)
        print(self.addlist)
        count={}
        for i in self.addlist:
            try: count[i] += 1
            except: count[i]=1
        print(count)
        tablectrl.addlist1(tableInfoWidget.NUM,count)
        self.addlist.clear()
        print(self.addlist)
        #self.windowExitF()
        print('주문 추가')

    def writeOnTable(self, name, price):
        card=self.billTablecard
        cash=self.billTablecash
        if type(self.isMenuOnTable(name)) == bool and self.isMenuOnTable(name) == False:
            amount = 1
            count = self.billTablerow
            #print(count)
            #print(name,str(amount),price,str(int(price)*amount))
            self.billWidget.setRowCount(count+1)
            self.billWidget.setItem(count,0,QTableWidgetItem(name))
            self.billWidget.setItem(count,1,QTableWidgetItem(str(amount)))
            self.billWidget.setItem(count,2,QTableWidgetItem(price))
            self.billWidget.setItem(count,3,QTableWidgetItem(str(int(price)*amount)))
            cash += int(price)
                    
            self.stateWidget.clearContents()
            self.stateWidget.setRowCount(1)
            self.stateWidget.setItem(0,0,QTableWidgetItem(str(card)))
            self.stateWidget.setItem(0,1,QTableWidgetItem(str(cash)))
            self.stateWidget.setItem(0,2,QTableWidgetItem(str(card+cash)))
            self.billTablecash = cash
            self.billTablerow += 1
        else:
            i = self.isMenuOnTable(name)
            amount = int(self.HowManyOnMenuTable(i))
            amount += 1
            self.billWidget.setItem(i, 1, QTableWidgetItem(str(amount)))  # 수량
            self.billWidget.setItem(i,3,QTableWidgetItem(str(int(price)*amount)))  # 합계
            cash += int(price)
            self.stateWidget.setRowCount(1)
            self.stateWidget.setItem(0,0,QTableWidgetItem(str(card)))
            self.stateWidget.setItem(0,1,QTableWidgetItem(str(cash)))
            self.stateWidget.setItem(0,2,QTableWidgetItem(str(card+cash)))
            self.billTablecash = cash
    
    def orderPaymentF(self):
        self.payDialog.setting(self.NUM)
        self.payDialog.show()
        #tablectrl.payment(tableInfoWidget.NUM)
        self.hide()
        print('결제')
    
    def windowExitF(self):
        self.menuWidget.clearContents()
        self.billWidget.clearContents()
        self.addlist.clear()
        tableInfoWidget().close()
        self.hide()


    

#if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   ob = tableInfoWidget()
#   ob.show()
#   sys.exit(app.exec_())
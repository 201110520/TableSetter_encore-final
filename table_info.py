import sys
from PyQt5 import uic
#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QPushButton, QApplication, QTableWidget, QTableWidgetItem, QWidget, QSpinBox
import POSvariable
from POSsql import Tablectrl

form_class = uic.loadUiType("table_info.ui")[0]


class tableInfoWidget(QDialog, form_class):
    menurow = 0 # menu창 row col
    menucol = 0
    billrow = 0 # 영수증화면 row col
    billcol = 0
    NUM = 0 #테이블번호
    billTablerow = 0
    billTablecard = 0
    billTablecash = 0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.orderDelete.clicked.connect(self.orderDeleteF)
        self.orderAdd.clicked.connect(self.orderAddF)
        self.orderPayment.clicked.connect(self.orderPaymentF)
        self.windowExit.clicked.connect(self.windowExitF)
        #self.menuWidget.verticalHeader().setVisible(False)
        #self.billWidget.verticalHeader().setVisible(False)
        #self.stateWidget.verticalHeader().setVisible(False)
        self.menuWidget.cellClicked.connect(self.menucolsave)
        self.billWidget.cellClicked.connect(self.billrowsave)
        self.menuWidget.cellClicked.connect(self.orderAddF)
        self.billWidget.cellClicked.connect(self.orderDeleteF)
        self.menuLoading()
        self.billLoading()
        self.orderAddF()
    
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
        row = Tablectrl.TableMenuLoad()
        count = len(row)
        self.menuWidget.setRowCount(count)
        for x in range(count):
            name, price, category = row[x]
            self.menuWidget.setItem(x,0,QTableWidgetItem(name))
            self.menuWidget.setItem(x,1,QTableWidgetItem(price))
        
    
    def billLoading(self):
        row=0
        row, card, cash = Tablectrl.billLoad(tableInfoWidget.NUM)
        self.billTablerow = len(row)
        self.billTablecard = card
        self.billTablecash = cash
        count = len(row)
        self.billWidget.setRowCount(count)
        for x in range(count):
            name, price, amount, paycode = row[x]
            self.billWidget.setItem(x,0,QTableWidgetItem(name))
            self.billWidget.setItem(x,1,QTableWidgetItem(str(amount)))
            self.billWidget.setItem(x,2,QTableWidgetItem(price))
            self.billWidget.setItem(x,3,QTableWidgetItem(str(int(price)*amount)))
        print(card,cash)
        self.stateWidget.setRowCount(1)
        self.stateWidget.setItem(0,0,QTableWidgetItem(str(card)))
        self.stateWidget.setItem(0,1,QTableWidgetItem(str(cash)))
        self.stateWidget.setItem(0,2,QTableWidgetItem(str((card+cash)-card)))
        print('영수증로딩')

    
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
        print(data)
        
        self.writeOnTable(data[0], data[1])
        #menuctrl.menuOpenClose(data)
        #self.billWidget.clearContents()
        #self.billLoading()
        print('주문 추가')

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

    def writeOnTable(self, name, price):
        card=self.billTablecard
        cash=self.billTablecash
        if type(self.isMenuOnTable(name)) == bool and self.isMenuOnTable(name) == False:
            amount = 1
            count = self.billTablerow+1
            print(count)
            print(name,str(amount),price,str(int(price)*amount))
            self.billWidget.setRowCount(count)
            for i in range(count):
                if self.billWidget.item(i, 0) != None:
                    print('와!',i)
                    print(self.billWidget.item(i, 0).text())
                    thing = self.billWidget.item(i,0)
                    if thing is not None and thing.text() == ' ':
                        self.billWidget.setItem(i,0,QTableWidgetItem(name))
                        self.billWidget.setItem(i,1,QTableWidgetItem(str(amount)))
                        self.billWidget.setItem(i,2,QTableWidgetItem(price))
                        self.billWidget.setItem(i,3,QTableWidgetItem(str(int(price)*amount)))
                        cash += int(price)
                        #self.totalAmount += amount
                        #self.totalPrice += price
                        break
                    
            #self.stateWidget.clearContents()
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
            self.billWidget.setItem(self.isMenuOnTable(name), 1, QTableWidgetItem(str(amount)))  # 수량
            self.billWidget.setItem(self.isMenuOnTable(name),3,QTableWidgetItem(str(int(price)*amount)))  # 합계
            cash += int(price)
            #self.totalAmount += 1
            #self.totalPrice += price
            #self.stateWidget.clearContents()
            self.stateWidget.setRowCount(1)
            self.stateWidget.setItem(0,0,QTableWidgetItem(str(card)))
            self.stateWidget.setItem(0,1,QTableWidgetItem(str(cash)))
            self.stateWidget.setItem(0,2,QTableWidgetItem(str(card+cash)))
            self.billTablecash = cash
    
    def orderPaymentF(self):
        Tablectrl.payment(tableInfoWidget.NUM)
        self.hide()
        print('결제')
    
    def windowExitF(self):
        self.menuWidget.setRowCount(0)
        self.billWidget.setRowCount(0)
        self.hide()


    

#if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   ob = tableInfoWidget()
#   ob.show()
#   exit(app.exec_())
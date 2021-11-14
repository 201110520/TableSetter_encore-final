import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from POSsql import AccCtrl
import datetime

accCtrl=AccCtrl()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('acc.ui')
form_class = uic.loadUiType(form)[0]

class accWidget(QWidget,form_class):
    def __init__(self, parent=None, ticker="acc"):
        super().__init__(parent)
        self.setupUi(self)
        self.acc_select_search.clicked.connect(self.selectShow)
        #self.calendarWidget.clicked.connect(self.syncdate)
        self.showAccounts()


    
    def showAccounts(self):
        self.clearAcc()
        date = datetime.datetime.now()
        curtime = date.strftime('%Y-%m-%d')
        curmonth = date.strftime('%Y-%m-')

        output_buf_1 = accCtrl.get_data_day(curtime)
        #output_buf_2 = accCtrl.get_data_day_method(curtime)
        acc_amount = accCtrl.get_amount(curtime)
        upper_day = accCtrl.get_method_day(curtime)
        upper_month = accCtrl.get_method_month(curmonth)

        #day_total_selling = accCtrl.get_day_total(curtime)
        self.acc_upper.setItem(0, 0, QTableWidgetItem(str(upper_day[2])))
        #month_total_selling = accCtrl.get_month_total(curmonth)
        self.acc_upper.setItem(0, 1, QTableWidgetItem(str(upper_day[0])))
        self.acc_upper.setItem(0, 2, QTableWidgetItem(str(upper_day[1])))

        self.acc_upper.setItem(1, 0, QTableWidgetItem(str(upper_month[2])))
        self.acc_upper.setItem(1, 1, QTableWidgetItem(str(upper_month[0])))
        self.acc_upper.setItem(1, 2, QTableWidgetItem(str(upper_month[1])))
        self.acc_main.setRowCount(acc_amount)
        for i in range(0, acc_amount):
            self.acc_main.setItem(i, 0, QTableWidgetItem(str(output_buf_1[i][0])))
            self.acc_main.setItem(i, 1, QTableWidgetItem(str(output_buf_1[i][1])))   
            if output_buf_1[i][2] == 1:
                self.acc_main.setItem(i, 2, QTableWidgetItem('모바일 결제'))
            else:
                self.acc_main.setItem(i, 2, QTableWidgetItem('현장 결제'))
             

    def selectShow(self):
        c_date = self.calendarWidget.selectedDate()
        
        c_date = str(c_date.toPyDate())
        output1 = accCtrl.get_data_day(c_date)
        output2 = accCtrl.get_data_day_method(c_date)
        output_amount = accCtrl.get_amount(c_date)

        self.clearAcc()
        self.acc_main.setRowCount(output_amount)
        for i in range(0, output_amount):
            self.acc_main.setItem(i, 0, QTableWidgetItem(str(output1[i][0])))
            self.acc_main.setItem(i, 1, QTableWidgetItem(str(output1[i][1])))
            if output1[i][2] == 1:
                self.acc_main.setItem(i, 2, QTableWidgetItem('모바일 결제'))
            else:
                self.acc_main.setItem(i, 2, QTableWidgetItem('현장 결제'))
        self.acc_main.resizeColumnsToContents()

        
        selected_day = accCtrl.get_method_day(c_date)
        self.acc_day_table.setRowCount(1)
        self.acc_day_table.setItem(0, 0, QTableWidgetItem(str(selected_day[2])))
        self.acc_day_table.setItem(0, 1, QTableWidgetItem(str(selected_day[0])))
        self.acc_day_table.setItem(0, 2, QTableWidgetItem(str(selected_day[1])))
        

    def syncdate(self):
        c_date = self.calendarWidget.selectedDate()
        self.dateEdit.date(c_date)
    def clearAcc(self):
        self.acc_main.setRowCount(0)
        self.acc_day_table.setRowCount(0)

    

#if __name__ == "__main__":
#    import sys
#    from PyQt5.QtWidgets import QApplication
#    app = QApplication(sys.argv)
#    ob = accWidget()
#    ob.show()
#    exit(app.exec_())

from PyQt5.QtCore import pyqtSignal
from POS import MainWindow
import sys
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from POSsql import LoginCtrl, AddUserCtrl


form_class2 = uic.loadUiType("login.ui")[0]
loginCtrl = LoginCtrl()
adduserctrl = AddUserCtrl()
login_re = POSvariable



class loginWindow(QMainWindow, form_class2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_Button.clicked.connect(self.logininfo)
        self.login_PW.setEchoMode(QLineEdit.Password)
        
    
    def logininfo(self):
            # ID, PW 입력받기
        id = self.login_ID.text()
        pw = self.login_PW.text()
        
        print(id,pw)
        # ID 와 PW 일치하는지 비교
        login_re.POS_ID, login_re.STORE_ID = loginCtrl.loginCheck(id, pw)
        if id == login_re.POS_ID:
            self.dialog = MainWindow(self)
            self.close()
            self.dialog.show()

        print('반환값', login_re.POS_ID,login_re.STORE_ID)
            
        return login_re.POS_ID , login_re.STORE_ID

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lw = loginWindow()
    lw.show()
    exit(app.exec_())
    
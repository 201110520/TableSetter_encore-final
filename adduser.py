import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from POSsql import AddUserCtrl

adduserctrl = AddUserCtrl()

form_class = uic.loadUiType("adduser.ui")[0]

class adduer_M(QDialog, form_class):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.userinput)
        self.btnCancel.clicked.connect(self.inputCancle)
        self.btnClear.clicked.connect(self.textClear)

    def userinput(self):
        ID = self.user_id.text()
        PW = self.user_pw.text()
        Explain = self.user_Explain.text()
        return_text = adduserctrl.AddUser(ID, PW, Explain)
        print(return_text)
        self.status.setText(return_text)

    def textClear(self):
        self.user_id.clear()
        self.user_pw.clear()
        self.user_Explain.clear()

    def inputCancle(self):
        self.close()
    


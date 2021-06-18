import sys
import os
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from POSsql import AddUserCtrl
from Crypto.PublicKey import RSA #pip3 install pycryptodome

adduserctrl = AddUserCtrl()

form_class = uic.loadUiType("CertificateStatusView.ui")[0]

class CertificateStatus_M(QDialog, form_class):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.CertificateSuccess.clicked.connect(self.createCertificate)
        self.CertificateSuccessExit.clicked.connect(self.exitWindow)

    def createFolder(self, direcroty):
        try:
            if not os.path.exists(direcroty):
                os.makedirs(direcroty)
        except OSError:
            print('ERROR: Creating directory.  ' + direcroty)

    
    def createCertificate(self):
        path2="'/Users/"+os.getenv('username')+"/.ssh'"
        print(path2)
        if not os.path.exists(path2):
            self.createFolder(path2)

        code = '12' #POSvariable.STORE_ID
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
        with open('C:/Users/'+os.getenv('username')+'/test/my_private_rsa_key.pem', 'wb') as f:
            f.write(encrypted_key)
        with open('C:/Users/'+os.getenv('username')+'/test/my_rsa_public.pem', 'wb') as f:
            f.write(key.publickey().exportKey())
        text = path2 + '경로에 my_private_rsa_key.pem, my_rsa_public.pem 가 생성되었습니다. '
        self.CertificateStatusView.setText(text)
    def exitWindow(self):
        self.close()
        print("닫기")
    

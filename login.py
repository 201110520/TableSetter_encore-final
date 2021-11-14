from PyQt5.QtCore import pyqtSignal
from POS import MainWindow
import sys
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from POSsql import LoginCtrl, AddUserCtrl
import os
#from pixmapTest import join_pixmap
import sys
import qrcode #pip3 install qrcode
import POSvariable
from PIL.ImageQt import ImageQt, Image #pip3 install Pillow? 다시 확인필요
from PyQt5 import uic , QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFont, QPixmap , QImage
from POSsql import LoginCtrl
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication
from POSvariable import TABLE_NUM
from table_info import tableInfoWidget
from POSsql import Tablectrl
import threading
import sys
from PyQt5 import uic
#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,QPushButton, QApplication, QTableWidget, QTableWidgetItem, QWidget, QSpinBox
import POSvariable
from POSsql import Tablectrl
import pymysql
import POSvariable
import time
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
import sys

from PyQt5.QtGui import QPixmap
import POSvariable
import urllib.request
from POSsql import Menuctrl
from imageS3Insert import imageS3Upload
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QWidget, QApplication, QTableWidget, QCheckBox
import boto3 #pip3 install boto3
import POSvariable
import sys
import os
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from POSsql import AddUserCtrl
from Crypto.PublicKey import RSA #pip3 install pycryptodome
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from POSsql import AddUserCtrl
from payment import paymodul
import sys
import os
import POSvariable
from PyQt5 import uic
from PyQt5.QtWidgets import QTabWidget,QPushButton,QLabel,QLineEdit, QDialog
from POSsql import Payctrl



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('login.ui')
form_class2 = uic.loadUiType(form)[0]

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
    sys.exit(app.exec_())
    
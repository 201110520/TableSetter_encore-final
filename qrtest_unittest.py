import sys
import os
import unittest
import PyQt5
import qrcode
from pyzbar.pyzbar import decode #pip3 install pyzbar
from PIL import Image
from unittest import IsolatedAsyncioTestCase
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QApplication
import POS, login, qr


app = QApplication(sys.argv)


class QRcreateTest(unittest.TestCase):

#1.pos 프로그램을 실행한다.    
    def setUp(self):
        self.loginform = login.loginWindow()
        self.posForm = POS.MainWindow()
        self.qrForm = qr.qrWidget()
#2.ID와 PW를 입력해 로그인한다.        
    def test_loginTest(self):

        self.loginform.login_ID.setText("nsj327")
        self.loginform.login_PW.setText("1234")
        self.assertEqual( (self.loginform.login_ID.text(),self.loginform.login_PW.text()) , self.loginform.login())
        loginTest = self.loginform.login_Button
        QTest.mouseClick(loginTest, Qt.LeftButton)       
#3.qr을 생성하기 위해선 왼쪽에 qr생성 버튼을 클릭한다.
    
        qrmenu = self.posForm.qr
        QTest.mouseClick(qrmenu, Qt.LeftButton)
        self.assertTrue(self.posForm.qr.setDisabled)
        
#3-1. 규격화된 크기의 원하는 배경 이미지를 등록한다.
#3-2. qr코드가 배경 이미지 위에 위치할 좌표의 x값을 입력한다.
#3-3. qr코드가 배경 이미지 위에 위치할 좌표의 y값을 입력한다.

#4.테이블 번호 입력 후 엔터 또는 생성 버튼을 클릭한다.
        self.qrForm.qrData.setText("13")
        qrcreateButton = self.qrForm.createQR
        QTest.mouseClick(qrcreateButton, Qt.LeftButton)

        current_dir = os.getcwd()
        file_name = self.qrForm.qrData.text()
        
        if file_name:
            self.qrForm.QRimage.pixmap().save(os.path.join(current_dir, file_name + '번 테이블.png'))
        img = Image.open('13번 테이블.png')
        result = decode(img)
        for i in result:
            data = i.data.decode("utf-8")

        self.assertEqual(data, 'store_id=34526 table_num='+self.qrForm.qrData.text())

#5.생성된 qr코드를 저장버튼을 눌러 저장한다.
        qrsaveButton = self.qrForm.saveQR
        QTest.mouseClick(qrsaveButton, Qt.LeftButton)
#6.
    def test_qrclear(self):
        qrclearButton = self.qrForm.clearQR
        QTest.mouseClick(qrclearButton, Qt.LeftButton)
        self.assertIsNone(self.qrForm.QRimage.pixmap())

 

if __name__ == '__main__':
    unittest.main()
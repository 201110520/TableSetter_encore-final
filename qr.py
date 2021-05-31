import os
from pixmapTest import join_pixmap
import sys
import qrcode #pip3 install qrcode
from PIL.ImageQt import ImageQt #pip3 install Pillow? 다시 확인필요
from PyQt5 import uic , QtCore
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFont, QPixmap , QImage

class qrWidget(QWidget):
    def __init__(self, parent=None, ticker="qr"):
        super().__init__(parent)
        uic.loadUi("qr.ui", self)
        self.createQR.clicked.connect(self.create_QR)
        self.saveQR.clicked.connect(self.save_QR)
        self.clearQR.clicked.connect(self.clear_QR)
        self.qrData.returnPressed.connect(self.create_QR)

    def create_QR(self):
        text = 'store_id=34526 table_num='+self.qrData.text()

        img = qrcode.make(text, box_size = 2)
        qr = ImageQt(img)
        pix = QPixmap.fromImage(qr)
        self.QRimage.setPixmap(pix)
    
    def save_QR(self) :
    
        current_dir = os.getcwd()
        file_name = self.qrData.text()
        
        if file_name:
            print(current_dir, file_name, "번 테이블.png")
            self.QRimage.pixmap().save(os.path.join(current_dir, file_name + '번 테이블.png'))
            
    
    def clear_QR(self) :
        self.qrData.clear()
        self.QRimage.clear()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ob = qrWidget()
    ob.show()
    exit(app.exec_())
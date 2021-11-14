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

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('qr.ui')
form_class = uic.loadUiType(form)[0]


loginCtrl = LoginCtrl()
login_re = POSvariable

class qrWidget(QWidget, form_class):
    def __init__(self, parent=None, ticker="qr"):
        super().__init__(parent)
        self.setupUi(self)
        self.createQR.clicked.connect(self.create_QR)
        self.saveQR.clicked.connect(self.save_QR)
        self.clearQR.clicked.connect(self.clear_QR)
        self.qrData.returnPressed.connect(self.create_QR)
        

    def create_QR(self):
        print(login_re.STORE_ID,login_re.POS_ID)
        text = {'store_id': login_re.STORE_ID  , 'table_num':  self.qrData.text() }
        print(text['store_id'],text['table_num'])
        img = qrcode.make(text, box_size = 3)
        qr = ImageQt(img)
        pix = QPixmap.fromImage(qr)
        self.QRimage.setPixmap(pix)
    
    def save_QR(self) : 
        current_dir = os.getcwd()
        file_name = self.qrData.text()
        
        if file_name:
            print(current_dir, file_name, "_table.png")
            self.QRimage.pixmap().save(os.path.join(current_dir, file_name + '_table.png'))
        
        images = [ Image.open("template.png") , Image.open(file_name + '_table.png') ]
        width = images[0].size[0]
        height = images[0].size[1]

        mergeImage = Image.new("RGB", (width, height),(255,255,255))
        xOffset = 0
        yOffset = 0
        for img in images:
            mergeImage.paste(img, (xOffset, yOffset))
            xOffset += 50
            yOffset += 100
        mergeImage.save(os.path.join(current_dir, file_name + '_table.png'))

    def clear_QR(self) :
        self.qrData.clear()
        self.QRimage.clear()
        


#if __name__ == "__main__":
#    
#    app = QApplication(sys.argv)
#    ob = qrWidget()
#    ob.show()
#    sys.exit(app.exec_())
import sys
import os
from PyQt5.QtGui import QPixmap
import POSvariable
import urllib.request
from POSsql import Menuctrl
from imageS3Insert import imageS3Upload
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QWidget, QApplication, QTableWidget, QCheckBox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('menu.ui')
form_class = uic.loadUiType(form)[0]

menuctrl = Menuctrl()
s3Upload = imageS3Upload()

class menuWidget(QWidget,form_class):
    row=0
    col=0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addButton.clicked.connect(self.foodAdd)
        self.clearButton.clicked.connect(self.foodClear)
        self.deleteButton.clicked.connect(self.foodDelete)
        self.modButton.clicked.connect(self.foodMod)
        self.foodClose.clicked.connect(self.foodopenClose)
        self.selectImage.clicked.connect(self.imageSelect)
        self.menuTableWidget.cellClicked.connect(self.cellclick)
        self.menuTableWidget.cellClicked.connect(self.rowsave)
        self.categorys()
        self.menuLoading()
    
    def rowsave(self, row, col):
        menuWidget.row = row
        menuWidget.col = col
        print(menuWidget.row,menuWidget.col)


    def categorys(self):
        row = menuctrl.cateinfo()
        print(row)
        self.catecomboBox.addItems(row)

    
    def menuLoading(self):
        rows, count = menuctrl.menuLoad()
        self.menuTableWidget.setRowCount(count)
        for x in range(count):
            self.checbox=QCheckBox()
            name, price, status = rows[x]
            self.menuTableWidget.setItem(x,0,QTableWidgetItem(name))
            self.menuTableWidget.setItem(x,1,QTableWidgetItem(price))
            if status >= 1:
                item = QTableWidgetItem()
                item.setCheckState(QtCore.Qt.Checked)
                self.menuTableWidget.setItem(x, 2, item)
            else:
                item = QTableWidgetItem()
                item.setCheckState(QtCore.Qt.Unchecked)
                self.menuTableWidget.setItem(x, 2, item)

    def cellclick(self, row, col):
        if col ==0:
            cell = self.menuTableWidget.item(row, col)
        else:
            cell = self.menuTableWidget.item(row, 0)
        print(cell.text())
        cellmenuName = str(cell.text())
        row = menuctrl.cellselet(cellmenuName)
        num, category, name, imageurl , price, description = row

        self.menuName.setText(name)
        self.menuprice.setText(price)
        self.catecomboBox.setCurrentText(category)
        self.fooddescription.setText(description)
        image = urllib.request.urlopen(imageurl).read()
        self.foodimages = QPixmap()
        self.foodimages.loadFromData(image)
        self.foodimages = self.foodimages.scaledToHeight(179)
        self.foodimage.setPixmap(self.foodimages)
        
        self.imagefilename.clear()
        

    def foodAdd(self):
        category = str(self.catecomboBox.currentText())
        name = self.menuName.text()
        price = self.menuprice.text()
        description = self.fooddescription.toPlainText()
        imageurl = self.imagefilename.text()
        rows = [category,name,price,description, imageurl]
        #print (name,rows,rows[0],rows[3])
        menuctrl.menuAdd(rows)
        s3Upload.imageUpload(imageurl)
        self.menuTableWidget.clearContents()
        self.menuLoading()
        #print('foodAdd')

    def foodClear(self):
        self.menuName.clear()
        self.menuprice.clear()
        self.fooddescription.clear()
        self.foodimage.clear()
        self.imagefilename.clear()
        #print('foodClear')
    
    def foodDelete(self):
        category = str(self.catecomboBox.currentText())
        name = self.menuName.text()
        rows = [ name, category]
        menuctrl.menuDelete(rows)
        self.menuTableWidget.clearContents()
        self.menuLoading()
        self.foodClear()
        #print('foodDelete')
    
    def foodMod(self):
        if menuWidget.col ==0:
            cell = self.menuTableWidget.item(menuWidget.row, menuWidget.col)
        else:
            cell = self.menuTableWidget.item(menuWidget.row, 0)
        Fname = str(cell.text())
        category = str(self.catecomboBox.currentText())
        name = self.menuName.text()
        price = self.menuprice.text()
        description = self.fooddescription.toPlainText()
        imageurl = self.imagefilename.text()
        #print(imageurl)
        if imageurl == '':
            rows=[name,price,description,category]
            menuctrl.menuModNoImage(Fname, rows)
            #print('이미지 유지')
        else:
            #print('이미지 수정')
            rows=[category,name,price,description,imageurl]
            #print(rows)
            menuctrl.menuMod(Fname,rows)
            s3Upload.imageUpload(imageurl)
            

        self.menuTableWidget.clearContents()
        self.menuLoading()
        self.cellclick(menuWidget.row,menuWidget.col)

        print('foodMod')
    
    def foodopenClose(self):
        row = menuWidget.row
        data = []
        for col in range(3):
            if col ==2:
                it = self.menuTableWidget.item(row,2)
                text = it.checkState()
                data.append(text)
            else:
                it = self.menuTableWidget.item(row, col)
                text = it.text() if it is not None else ""
                data.append(text)
        print(data)
        menuctrl.menuOpenClose(data)
        self.menuTableWidget.clearContents()
        self.menuLoading()
        print('foodClose')
    
    def imageSelect(self):
        fname = QFileDialog.getOpenFileName(self)
        self.imagefilename.setText(fname[0])
        self.foodimages = QPixmap()
        self.foodimages.load(fname[0])
        self.foodimages = self.foodimages.scaledToHeight(179)
        self.foodimage.setPixmap(self.foodimages)
        print('imageSelect')


#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    ob = menuWidget()
#    ob.show()
#    sys.exit(app.exec_())
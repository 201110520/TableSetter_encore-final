import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class menuWidget(QWidget):
    def __init__(self, parent=None, ticker="menu"):
        super().__init__(parent)
        uic.loadUi("menu.ui", self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ob = menuWidget()
    ob.show()
    exit(app.exec_())
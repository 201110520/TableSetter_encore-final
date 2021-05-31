import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class accWidget(QWidget):
    def __init__(self, parent=None, ticker="acc"):
        super().__init__(parent)
        uic.loadUi("acc.ui", self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ob = accWidget()
    ob.show()
    exit(app.exec_())
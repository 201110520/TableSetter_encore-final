import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class tableInfoWidget(QWidget):
    def __init__(self, parent=None, ticker="table"):
        super().__init__(parent)
        uic.loadUi("table_info.ui", self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ob = tableInfoWidget()
    ob.show()
    exit(app.exec_())
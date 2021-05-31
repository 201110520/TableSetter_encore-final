import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

def __init__(self, dataitem, parent=None):
        super(otherPanel, self).__init__(parent)
        self.setFrameStyle(widgets.QFrame.Sunken)
        self.setFrameShape(widgets.QFrame.Box)
        self.data = dataitem

        layout = widgets.QGridLayout()
        labelnob = widgets.QLabel(_("Number of bytes"))
        lableunit = widgets.QLabel(_("Unit"))

        layout.addWidget(labelnob, 0, 0)
        layout.addWidget(lableunit, 1, 0)
        layout.setRowStretch(2, 1)

        self.inputnob = widgets.QSpinBox()
        self.inputnob.setRange(1, 10240)
        self.inputtype = widgets.QComboBox()
        self.inputtype.addItem("ASCII")
        self.inputtype.addItem("BCD/HEX")

        layout.addWidget(self.inputnob, 0, 1)
        layout.addWidget(self.inputtype, 1, 1)

        self.setLayout(layout)
        self.init() 
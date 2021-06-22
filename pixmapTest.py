#import sys
#from PyQt5 import QtCore, QtGui, QtWidgets
#
#def join_pixmap(p1, p2, mode=QtGui.QPainter.CompositionMode_SourceOver):
#    s = p1.size().expandedTo(p2.size())
#    result =  QtGui.QPixmap(s)
#    result.fill(QtCore.Qt.transparent)
#    painter = QtGui.QPainter(result)
#    painter.setRenderHint(QtGui.QPainter.Antialiasing)
#    painter.drawPixmap(QtCore.QPoint(), p1)
#    painter.setCompositionMode(mode)
#    painter.drawPixmap(result.rect(), p2, p2.rect())
#    painter.end()
#    return result
#
#class Viewer(QtWidgets.QGraphicsView):
#    def __init__(self, parent=None):
#        super(Viewer, self).__init__(parent)
#        self._scene = QtWidgets.QGraphicsScene(self)
#        self.setScene(self._scene)  
#
#        blue = QtGui.QPixmap(200, 200) 
#        blue.fill(QtCore.Qt.transparent)
#        p = QtGui.QPainter(blue)
#        pen = QtGui.QPen(QtGui.QBrush(QtGui.QColor(0,0,255)), 10)
#        p.setPen(pen)
#        p.drawLine(0, 0, 100, 100)
#        p.end()
#        self.photo = self._scene.addPixmap(blue)
#
#        green = QtGui.QPixmap(100, 100)
#        green.fill(QtCore.Qt.transparent)            
#        p = QtGui.QPainter(green)
#        pen = QtGui.QPen(QtGui.QBrush(QtGui.QColor(0, 255, 0, 255)), 10)
#        p.setPen(pen)
#        p.drawLine(100, 0, 0, 100)
#        p.end()
#        self.label = self._scene.addPixmap(green) 
#        self.label.setPos(200, 0)     
#
#        self.overlayMaps()
#
#    def overlayMaps(self):
#        p1 = QtGui.QPixmap(self.photo.pixmap())
#        p2 = QtGui.QPixmap(self.label.pixmap())
#
#        result_pixmap = join_pixmap(self.photo.pixmap(), self.label.pixmap())
#        self.result_item = self._scene.addPixmap(result_pixmap)
#        self.result_item.setPos(100, 200)
#
#        result_pixmap.save("result_pixmap.png")
#
#if __name__ == '__main__':
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    window = Viewer()
#    window.resize(640, 480)
#    window.show()
#    sys.exit(app.exec_())
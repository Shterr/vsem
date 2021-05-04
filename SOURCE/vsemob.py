#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import vsemui

class myWindow(QtWidgets.QTabWidget):
    def __init__(self, parent = None):
        QtWidgets.QTabWidget.__init__(self,parent)
        self.myWidget = vsemui.Ui_TabWidget()
        self.myWidget.setupUi(self)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myWindow()
    window.show()
    sys.exit(app.exec_())
    

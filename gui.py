# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:31:38 2016

@author: Wichpong
"""

import sys
from PyQt5 import QtCore, QtGui, uic

qtCreatorFile = "test1.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

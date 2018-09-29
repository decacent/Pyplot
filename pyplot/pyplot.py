#!/usr/bin/env python

# encoding: utf-8

'''

@author: decacent

@license: Copyright (C) 2017-2018 decacent. All rights reserved.

@contact: shaochuang_routine@outlook.com

@software: pycharm

@file: pyplot.py

@time: 2018/9/28 20:57

@desc:

'''

import os
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from ui.main_ui import Ui_MainWindow
from ui.cavas2D import Ui_Form
from form.sheet import Sheet


class ChildrenForm2(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm2, self).__init__()
        self.setupUi(self)
        self.figure1 = plt.figure(facecolor='#ecf0f1')
        self.ax1 = self.figure1.add_subplot(111)
        self.figure1.subplots_adjust(left=0.08, right=0.95, top=0.98)
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.verticalLayout.addWidget(self.toolbar1)
        self.verticalLayout.addWidget(self.canvas1)


class Mywin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionClose.triggered.connect(self.test)

        self.data = None

    def openFile(self):
        fn, ok = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.csv)")
        a = np.loadtxt(fn, skiprows=0, delimiter=',')

        self.data = a

        print(self.data)

        new_sheet = Sheet(self.data.shape[0], self.data.shape[1])
        new_sheet.setWindowTitle('Sheet 1')
        self.mdiArea.addSubWindow(new_sheet)
        print('gg')
        new_sheet.show()

    def test(self):
        subwindow3 = ChildrenForm2()
        subwindow3.setWindowTitle('Figure %d' % subwindow3.figure1.number)
        subwindow3.ax1.plot(np.arange(5))
        self.mdiArea.addSubWindow(subwindow3)
        subwindow3.show()

        # self.dd=ChildrenForm()
        # # t = np.arange(0.0, 3.0, 0.01)
        # # self.dd.ax1.plot(t)
        # # self.dd.canvas1.draw()
        # self.mdiArea.addSubWindow(self.dd)


app = QApplication(sys.argv)
main = Mywin()
main.show()
app.exec_()

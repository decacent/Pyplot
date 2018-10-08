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
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from ui.main_ui import Ui_MainWindow
from ui.cavas2D import Ui_Form
# from form.sheet import MyTable
from ui.table_ui import TableSheet
from pandas import read_csv
from spyder.widgets.variableexplorer.dataframeeditor import DataFrameEditor, DataFrameView
from spyder.widgets.variableexplorer.arrayeditor import ArrayView, ArrayModel, ArrayEditorWidget
from spyder.widgets.variableexplorer.importwizard import ContentsWidget, PreviewTableModel, PreviewTable, PreviewWidget, \
    ImportWizard
from PyQt5.QtWidgets import QTableWidget


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
        self.actionSave.triggered.connect(self.creat_none_table)
        self.actionImport.triggered.connect(self.importdata)
        self.figurepool = []
        self.sheetpool = []

        self.data = None
        self.sheet_count = 0
        self.figure_count = 0

        self.sheet_pool = {}
        self.figure_pool = {}

        self.creat_none_table()

        self.mdiArea.subWindowActivated.connect(self.get_mdiWindow)

    def get_mdiWindow(self):
        print(self.mdiArea.currentSubWindow().windowTitle())

    # self.mdiArea.
    def creat_none_table(self):
        self.creat_table(data=None)

    def creat_table(self, data):
        new_sheet = TableSheet(data=data, count=self.sheet_count)
        self.sheet_count += 1
        self.sheet_pool.update({'sheet{}'.format(self.sheet_count): {'target': new_sheet, 'data': data,
                                                                     'window': self.mdiArea.currentSubWindow()}})
        new_sheet.setWindowTitle('Sheet {}'.format(self.sheet_count))
        self.mdiArea.addSubWindow(new_sheet)
        self.sheet_pool['sheet{}'.format(self.sheet_count)]['target'].show()

    def openFile(self):
        fn, ok = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.csv)")
        print(ok)
        a = np.loadtxt(fn, skiprows=0, delimiter=',')
        df = read_csv(fn, index_col=None, header=0)

        self.data = a
        self.creat_table(a)

        # print(self.data)

    #  new_sheet = QTableWidget()
    #  new_sheet.setWindowTitle('Sheet 1')
    #  new_sheet.setColumnCount(self.data.shape[1])
    #  new_sheet.setRowCount(self.data.shape[0])
    #  for i in range(len(df.index)):
    #      for j in range(len(df.columns)):
    #          try:
    #              new_sheet.setItem(i, j, QTableWidgetItem(str(float((df.iloc[i, j])))))
    #          except:
    #              pass
    #  self.mdiArea.addSubWindow(new_sheet)
    #  new_sheet.show()

    def test(self):
        print(self.s.model.xlabels)
        self.new_sheet.setHorizontalHeaderLabels(['x', 'y1', 'y2'])
        self.new_sheet.reset()
        self.new_sheet.show()

        # subwindow3 = ChildrenForm2()
        # subwindow3.setWindowTitle('Figure %d' % subwindow3.figure1.number)
        # subwindow3.ax1.plot(np.arange(5))
        # self.mdiArea.addSubWindow(subwindow3)
        # subwindow3.show()
        # a=self.s.view.selectedIndexes()
        # print(type(a))
        # #print(a)
        # print(a[0])
        # print(a[0].data(),a[0].row(),a[0].column())

        print('gg')

    def importdata(self):
        fn, ok = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.csv)")
        # file_object = open('test.txt', 'rU')
        with open(fn, "r") as f:  # 设置文件对象
            str = f.read()
        importdata = ImportWizard(None, str)
        if importdata.exec_():
            var_name, clip_data = importdata.get_data()
        type(clip_data)

        # a=self.importdata.get_data()
        self.creat_table(np.array(clip_data))


app = QApplication(sys.argv)
main = Mywin()
main.show()
app.exec_()

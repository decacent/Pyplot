#!/usr/bin/env python

# encoding: utf-8

'''

@author: decacent

@license: Copyright (C) 2017-2018 decacent. All rights reserved.

@contact: shaochuang_routine@outlook.com

@software: pycharm

@file: sheet.py

@time: 2018/9/28 22:19

@desc:

'''
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from pandas import read_csv
from spyder.widgets.variableexplorer.dataframeeditor import DataFrameEditor, DataFrameView
from form.arrayeditor import ArrayView, ArrayModel, ArrayEditorWidget


class MyTable(ArrayEditorWidget):
    def __init__(self, data, xlabels, parent=None):
        super(MyTable, self).__init__(parent, data,xlabels)
        self.setWindowTitle('Sheet 1')
        # self.setWindowIcon(QIcon("male.png"))
        # self.resize(920, 240)
        #self.model.xlabels=xlabels
        self.model.__init__(data=data,xlabels=xlabels)
        #self.model.__init__(data=data,xlabels= self.xlabels)
        #self.data = data
        self.column = self.model.total_cols
        self.row = self.model.total_rows
        print(self.column, self.row)
        self.header = ['x']
        #self.xlabels = xlabel
        self.header.extend(['y' + str(x + 1) for x in range(self.column)])
        # self.model.setHorizontalHeaderLabels(['x','y1','y2'])
        # self.view.setHorizontalHeader(self.header)
        # print(self.model.headerData())
        # self.model.
        # self.setColumnCount(5)
        # self.setRowCount(2)
        # self.setSelectionBehavior(QTableWidget.SelectColumns)
        # self.setSelectionMode(QTableWidget.MultiSelection)
        # 设置表格有两行五列。
        # self.setColumnWidth(0, 200)
        # self.setColumnWidth(4, 200)
        # self.setRowHeight(0, 100)
        # 设置第一行高度为100px，第一列宽度为200px。

    def getSelectedData(self):
        selectedtable = self.view.selectedIndexes()
        # self.view.horizontalHeader()
        # self.view.setHorizontalHeader()
        # self.
        # print(type(a))
        # # print(a)
        # print(a[0])
        # print(a[0].data(), a[0].row(), a[0].column())
        #
        # s_row,s_col=[],[]
        # for i in

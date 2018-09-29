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

from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets




class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("我是一个表格")
        #self.setWindowIcon(QIcon("male.png"))
        #self.resize(920, 240)
        self.setColumnCount(5)
        self.setRowCount(2)
        self.setSelectionBehavior(QTableWidget.SelectColumns)
        self.setSelectionMode(QTableWidget.MultiSelection)
        # 设置表格有两行五列。
        #self.setColumnWidth(0, 200)
        #self.setColumnWidth(4, 200)
        #self.setRowHeight(0, 100)
        # 设置第一行高度为100px，第一列宽度为200px。



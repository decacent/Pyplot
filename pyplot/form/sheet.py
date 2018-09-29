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

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.table_ui import Ui_sheet


class Sheet(QtWidgets.QWidget, Ui_sheet):
    def __init__(self, row, column):
        super(Sheet, self).__init__()
        self.row = row
        self.column = column
        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.setRowCount(2)
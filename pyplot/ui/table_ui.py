# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import  sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem,QHBoxLayout


class TableSheet(QtWidgets.QWidget):
    def __init__(self,data,count):
        super().__init__()
        self.data = data
        if self.data is None:
            self.col = 5
            self.row = 100
        else:
            self.col = self.data.shape[1]
            self.row = self.data.shape[0]

        new_sheet = QTableWidget()
        new_sheet.setWindowTitle('Sheet {}'.format(count))
        new_sheet.setColumnCount(self.col)
        new_sheet.setRowCount(self.row)
        for i in range(self.row):
            for j in range(self.col):
                try:
                    new_sheet.setItem(i, j, QTableWidgetItem(str(float((self.data[i, j])))))
                except:
                    pass
        header = ['x']
        header.extend(['y' + str(x + 1) for x in range(self.col)])
        new_sheet.setWindowTitle('Sheet 1')
        new_sheet.setHorizontalHeaderLabels(header)
        # new_sheet.show()

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(new_sheet)
        self.setLayout(mainLayout)



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sheet(object):
    def setupUi(self, sheet):
        sheet.setObjectName("sheet")
        sheet.resize(633, 516)
        self.horizontalLayout = QtWidgets.QHBoxLayout(sheet)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(sheet)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(sheet)
        QtCore.QMetaObject.connectSlotsByName(sheet)

    def retranslateUi(self, sheet):
        _translate = QtCore.QCoreApplication.translate
        sheet.setWindowTitle(_translate("sheet", "Sheet"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("sheet", "r1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("sheet", "r2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("sheet", "x"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("sheet", "y"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
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
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(sheet)
        QtCore.QMetaObject.connectSlotsByName(sheet)

    def retranslateUi(self, sheet):
        _translate = QtCore.QCoreApplication.translate
        sheet.setWindowTitle(_translate("sheet", "Sheet"))


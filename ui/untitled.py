# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 832)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.horizontalLayout_4.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDfd = QtWidgets.QMenu(self.menubar)
        self.menuDfd.setObjectName("menuDfd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(30, 30))
        self.toolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.toolBar.setStyleSheet("QToolBar {\n"
"    background-color: rgb(191, 191, 191);\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    image: url(handle.png);\n"
"}")
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.dockWidget_11 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_11.setObjectName("dockWidget_11")
        self.dockWidgetContents_11 = QtWidgets.QWidget()
        self.dockWidgetContents_11.setObjectName("dockWidgetContents_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_11)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView_3 = QtWidgets.QListView(self.dockWidgetContents_11)
        self.listView_3.setObjectName("listView_3")
        self.verticalLayout_2.addWidget(self.listView_3)
        self.dockWidget_11.setWidget(self.dockWidgetContents_11)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_11)
        self.dockWidget_12 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_12.setObjectName("dockWidget_12")
        self.dockWidgetContents_12 = QtWidgets.QWidget()
        self.dockWidgetContents_12.setObjectName("dockWidgetContents_12")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_12)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView_4 = QtWidgets.QListView(self.dockWidgetContents_12)
        self.listView_4.setObjectName("listView_4")
        self.verticalLayout.addWidget(self.listView_4)
        self.dockWidget_12.setWidget(self.dockWidgetContents_12)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_12)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        self.actionOpen.setEnabled(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.dakai = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img47s.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/img4.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/img/img45s.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/img1.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/img47.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/img/img10.ico"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.dakai.setIcon(icon)
        self.dakai.setObjectName("dakai")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDfd.menuAction())
        self.toolBar.addAction(self.dakai)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDfd.setTitle(_translate("MainWindow", "dfd"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionClose.setText(_translate("MainWindow", "close"))
        self.dakai.setText(_translate("MainWindow", "action"))

# import tool.images
from PyQt5.QtWidgets import QApplication,QMainWindow
import  sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import  numpy as np
from matplotlib.figure import Figure
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        # self.toolbar1 = NavigationToolbar(FigureCanvas,self)

        self.setParent(parent)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # FigureCanvas.setSizePolicy(sizePolicy)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyStaticMplCanvas(MyMplCanvas):
    """静态画布：一条正弦线"""
    def compute_initial_figure(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)
        self.axes.plot(t, s)


class ChildrenForm(Ui_Form):
    def __init__(self,x,y):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)
        self.canvas1=MyStaticMplCanvas()
        # self.verticalLayout.addWidget(self.canvas1.toolbar1)
        # self.verticalLayout.addWidget(self.canvas1)


class ChildrenForm2(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(ChildrenForm2,self).__init__()
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
        super(Mywin, self).__init__(parent)
        self.setupUi(self)
        self.main_widget = QtWidgets.QWidget(self)
        # self.subwindow2= MyMplCanvas
        # self.mdiArea.addSubWindow(self.subwindow2)

        self.dakai.triggered.connect(self.dsd)
        # self.subwindow3 = ChildrenForm()

    def dsd(self):
        subwindow3 = ChildrenForm2()
        subwindow3.setWindowTitle('Figure %d' %subwindow3.figure1.number)
        subwindow3.ax1.plot(np.arange(5))
        self.mdiArea.addSubWindow(subwindow3)
        subwindow3.show()

        # self.dd=ChildrenForm()
        # # t = np.arange(0.0, 3.0, 0.01)
        # # self.dd.ax1.plot(t)
        # # self.dd.canvas1.draw()
        # self.mdiArea.addSubWindow(self.dd)




app=QApplication(sys.argv)
main=Mywin()
main.show()
app.exec_()
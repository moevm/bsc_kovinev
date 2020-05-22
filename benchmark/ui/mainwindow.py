# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_raw/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(216, 157)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout_widgets = QtWidgets.QHBoxLayout()
        self.layout_widgets.setObjectName("layout_widgets")
        self.verticalLayout_2.addLayout(self.layout_widgets)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 216, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Model = QtWidgets.QAction(MainWindow)
        self.actionAdd_Model.setObjectName("actionAdd_Model")
        self.menuAdd.addAction(self.actionAdd_Model)
        self.menubar.addAction(self.menuAdd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D Models Comparison"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.actionAdd_Model.setText(_translate("MainWindow", "Add Model"))
        self.actionAdd_Model.setShortcut(_translate("MainWindow", "Ctrl+Shift+M"))



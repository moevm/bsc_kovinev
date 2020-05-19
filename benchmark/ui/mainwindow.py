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
        MainWindow.resize(159, 123)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 159, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuInstall = QtWidgets.QMenu(self.menubar)
        self.menuInstall.setObjectName("menuInstall")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Software = QtWidgets.QAction(MainWindow)
        self.actionAdd_Software.setObjectName("actionAdd_Software")
        self.actionCheck_exists = QtWidgets.QAction(MainWindow)
        self.actionCheck_exists.setObjectName("actionCheck_exists")
        self.actionCheck_build = QtWidgets.QAction(MainWindow)
        self.actionCheck_build.setObjectName("actionCheck_build")
        self.actionAdd_Model = QtWidgets.QAction(MainWindow)
        self.actionAdd_Model.setObjectName("actionAdd_Model")
        self.actionInstall_Software = QtWidgets.QAction(MainWindow)
        self.actionInstall_Software.setObjectName("actionInstall_Software")
        self.menuAdd.addAction(self.actionAdd_Software)
        self.menuAdd.addAction(self.actionAdd_Model)
        self.menuInstall.addAction(self.actionInstall_Software)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuInstall.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D Models Comparison"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menuInstall.setTitle(_translate("MainWindow", "Download"))
        self.actionAdd_Software.setText(_translate("MainWindow", "Add Software"))
        self.actionAdd_Software.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionCheck_exists.setText(_translate("MainWindow", "Check exists"))
        self.actionCheck_build.setText(_translate("MainWindow", "Check build"))
        self.actionAdd_Model.setText(_translate("MainWindow", "Add Model"))
        self.actionAdd_Model.setShortcut(_translate("MainWindow", "Ctrl+Shift+M"))
        self.actionInstall_Software.setText(_translate("MainWindow", "Install Software"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_raw/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_widgets = QtWidgets.QHBoxLayout()
        self.layout_widgets.setObjectName("layout_widgets")
        self.verticalLayout.addLayout(self.layout_widgets)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuCheck = QtWidgets.QMenu(self.menubar)
        self.menuCheck.setObjectName("menuCheck")
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
        self.menuAdd.addAction(self.actionAdd_Software)
        self.menuCheck.addAction(self.actionCheck_exists)
        self.menuCheck.addAction(self.actionCheck_build)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuCheck.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Some processing stuff"))
        self.pushButton.setText(_translate("MainWindow", "Some buttons like start"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuCheck.setTitle(_translate("MainWindow", "Check"))
        self.actionAdd_Software.setText(_translate("MainWindow", "Add Software"))
        self.actionCheck_exists.setText(_translate("MainWindow", "Check exists"))
        self.actionCheck_build.setText(_translate("MainWindow", "Check build"))


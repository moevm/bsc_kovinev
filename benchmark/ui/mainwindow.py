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
        MainWindow.resize(237, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_6.addWidget(self.plainTextEdit)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout_widgets = QtWidgets.QHBoxLayout()
        self.layout_widgets.setObjectName("layout_widgets")
        self.verticalLayout_2.addLayout(self.layout_widgets)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 237, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuCheck = QtWidgets.QMenu(self.menubar)
        self.menuCheck.setObjectName("menuCheck")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
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
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select image dir:"))
        self.groupBox.setTitle(_translate("MainWindow", "Images:"))
        self.label_4.setText(_translate("MainWindow", "Some processing stuff"))
        self.pushButton_2.setText(_translate("MainWindow", "Some buttons like start"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuCheck.setTitle(_translate("MainWindow", "Build"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionAdd_Software.setText(_translate("MainWindow", "Add Software"))
        self.actionCheck_exists.setText(_translate("MainWindow", "Check exists"))
        self.actionCheck_build.setText(_translate("MainWindow", "Check build"))


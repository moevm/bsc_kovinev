# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_raw/install_software_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 215)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_select = QtWidgets.QLabel(Dialog)
        self.label_select.setObjectName("label_select")
        self.verticalLayout_2.addWidget(self.label_select)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_path = QtWidgets.QLabel(Dialog)
        self.label_path.setObjectName("label_path")
        self.verticalLayout_3.addWidget(self.label_path)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_install = QtWidgets.QPushButton(Dialog)
        self.button_install.setObjectName("button_install")
        self.verticalLayout_4.addWidget(self.button_install)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setObjectName("label_status")
        self.verticalLayout_5.addWidget(self.label_status)
        self.progress = QtWidgets.QProgressBar(Dialog)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.verticalLayout_5.addWidget(self.progress)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Install Software"))
        self.label_select.setText(_translate("Dialog", "Select software to install: "))
        self.label_path.setText(_translate("Dialog", "Select path to install:"))
        self.button_install.setText(_translate("Dialog", "Install"))
        self.label_status.setText(_translate("Dialog", "Status:"))



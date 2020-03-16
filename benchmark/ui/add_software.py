# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_raw/add_software.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_software_name = QtWidgets.QLabel(Dialog)
        self.label_software_name.setObjectName("label_software_name")
        self.verticalLayout_2.addWidget(self.label_software_name)
        self.edit_software_nae = QtWidgets.QLineEdit(Dialog)
        self.edit_software_nae.setObjectName("edit_software_nae")
        self.verticalLayout_2.addWidget(self.edit_software_nae)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_software_run_command = QtWidgets.QLabel(Dialog)
        self.label_software_run_command.setObjectName("label_software_run_command")
        self.verticalLayout_3.addWidget(self.label_software_run_command)
        self.edit_software_run_command = QtWidgets.QLineEdit(Dialog)
        self.edit_software_run_command.setObjectName("edit_software_run_command")
        self.verticalLayout_3.addWidget(self.edit_software_run_command)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add = QtWidgets.QPushButton(Dialog)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_software_name.setText(_translate("Dialog", "Enter software name:"))
        self.edit_software_nae.setPlaceholderText(_translate("Dialog", "Meshroom"))
        self.label_software_run_command.setText(_translate("Dialog", "Enter run command:"))
        self.edit_software_run_command.setPlaceholderText(_translate("Dialog", "python app --input $1 --output $2 "))
        self.label.setText(_translate("Dialog", "Set:\n"
"- Input path with image: $1\n"
"- Output dir: $2"))
        self.button_add.setText(_translate("Dialog", "Add"))
        self.button_cancel.setText(_translate("Dialog", "Cancel"))


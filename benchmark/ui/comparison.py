# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_raw/comparison.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 134)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_select = QtWidgets.QComboBox(Dialog)
        self.comboBox_select.setObjectName("comboBox_select")
        self.horizontalLayout_2.addWidget(self.comboBox_select)
        self.compare_button = QtWidgets.QPushButton(Dialog)
        self.compare_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.compare_button.setObjectName("compare_button")
        self.horizontalLayout_2.addWidget(self.compare_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_left = QtWidgets.QLabel(Dialog)
        self.label_left.setText("")
        self.label_left.setObjectName("label_left")
        self.verticalLayout_3.addWidget(self.label_left)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_right = QtWidgets.QLabel(Dialog)
        self.label_right.setText("")
        self.label_right.setObjectName("label_right")
        self.verticalLayout_4.addWidget(self.label_right)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.table_layout = QtWidgets.QVBoxLayout()
        self.table_layout.setObjectName("table_layout")
        self.verticalLayout.addLayout(self.table_layout)
        self.label_down = QtWidgets.QLabel(Dialog)
        self.label_down.setObjectName("label_down")
        self.verticalLayout.addWidget(self.label_down)
        self.metrics_layout = QtWidgets.QVBoxLayout()
        self.metrics_layout.setObjectName("metrics_layout")
        self.verticalLayout.addLayout(self.metrics_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Compare Models"))
        self.compare_button.setText(_translate("Dialog", "Compare"))
        self.label.setText(_translate("Dialog", "Current model:"))
        self.label_2.setText(_translate("Dialog", "Selected model:"))
        self.label_down.setText(_translate("Dialog", "1"))



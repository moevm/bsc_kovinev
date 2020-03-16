# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui_raw/model.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 347)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_object_name = QtWidgets.QLabel(Form)
        self.label_object_name.setObjectName("label_object_name")
        self.verticalLayout_6.addWidget(self.label_object_name)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_rotate_x = QtWidgets.QLabel(Form)
        self.label_rotate_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_rotate_x.setObjectName("label_rotate_x")
        self.verticalLayout_4.addWidget(self.label_rotate_x)
        self.slider_rotate_x = QtWidgets.QSlider(Form)
        self.slider_rotate_x.setMaximumSize(QtCore.QSize(200, 16777215))
        self.slider_rotate_x.setOrientation(QtCore.Qt.Horizontal)
        self.slider_rotate_x.setObjectName("slider_rotate_x")
        self.verticalLayout_4.addWidget(self.slider_rotate_x)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_rotate_y = QtWidgets.QLabel(Form)
        self.label_rotate_y.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_rotate_y.setObjectName("label_rotate_y")
        self.verticalLayout_5.addWidget(self.label_rotate_y)
        self.slider_rotate_y = QtWidgets.QSlider(Form)
        self.slider_rotate_y.setMaximumSize(QtCore.QSize(200, 16777215))
        self.slider_rotate_y.setOrientation(QtCore.Qt.Horizontal)
        self.slider_rotate_y.setObjectName("slider_rotate_y")
        self.verticalLayout_5.addWidget(self.slider_rotate_y)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_rotate_z = QtWidgets.QLabel(Form)
        self.label_rotate_z.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_rotate_z.setObjectName("label_rotate_z")
        self.verticalLayout_3.addWidget(self.label_rotate_z)
        self.slider_rotate_z = QtWidgets.QSlider(Form)
        self.slider_rotate_z.setMaximumSize(QtCore.QSize(200, 16777215))
        self.slider_rotate_z.setOrientation(QtCore.Qt.Horizontal)
        self.slider_rotate_z.setObjectName("slider_rotate_z")
        self.verticalLayout_3.addWidget(self.slider_rotate_z)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_model = QtWidgets.QWidget(Form)
        self.widget_model.setMinimumSize(QtCore.QSize(300, 300))
        self.widget_model.setObjectName("widget_model")
        self.verticalLayout.addWidget(self.widget_model)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_object_name.setText(_translate("Form", "Title"))
        self.label_rotate_x.setText(_translate("Form", "Rotate X"))
        self.label_rotate_y.setText(_translate("Form", "Rotate Y"))
        self.label_rotate_z.setText(_translate("Form", "Rotate Z"))


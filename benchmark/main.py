import sys


import benchmark.ui.mainwindow
import benchmark.ui.add_software
import benchmark.ui.model

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from benchmark.model.model3D import Model3D
from benchmark.panda3dwidget.ModelView import ModelView
from benchmark.panda3dwidget.PandaWidget import PandaWidget


class MainWindowApp(QtWidgets.QMainWindow, benchmark.ui.mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_buttons()

    def init_buttons(self):
        self.actionAdd_Software.triggered.connect(self.f)
        self.actionAdd_Model.triggered.connect(self.add_model)

    def add_model(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Model files (*.obj)")
        print("[+] Filename passed from QFileDialog:", fname)
        m = Model3D(fname[0])
        widget = ModelWidget(self, m)
        self.layout_widgets.addWidget(widget)

    def f(self):
        dialog = AddSoftwareDialog(self)


class AddSoftwareDialog(QtWidgets.QDialog, benchmark.ui.add_software.Ui_Dialog):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)

        self.mainwindow = mainwindow

        self.init_buttons()

        self.show()
        self.exec_()

    def init_buttons(self):
        self.button_cancel.clicked.connect(self.close_dialog)
        self.button_add.clicked.connect(self.add_widget)

        self.comboBox_select_default.addItems(["/home/alien/Desktop/diploma/models/house_red/zephyr/zephyr.obj",
                                               "/home/alien/Desktop/diploma/models/house_red/meshroom/texturedMesh.obj"])

    def close_dialog(self):
        self.close()

    def add_widget(self):
        widget = ModelWidget(self, Model3D(self.comboBox_select_default.currentText()))
        self.mainwindow.layout_widgets.addWidget(widget)


class ModelWidget(QtWidgets.QWidget, benchmark.ui.model.Ui_Form):
    def __init__(self, parent, model):
        super().__init__()
        self.parent = parent
        self.setupUi(self)


        self.label_object_name.setText("Model: " + model.filename.split("/")[-1])
        self.modelView = ModelView(model.filename)
        self.widget = PandaWidget(self.modelView, self.label_model_info)
        self.verticalLayout.addWidget(self.widget)

        self.init_buttons()

    def init_buttons(self):
        self.slider_rotate_x.valueChanged.connect(self.slider_changed_x)
        self.slider_rotate_y.valueChanged.connect(self.slider_changed_y)



    def slider_changed_x(self):
        self.modelView.camera_controller.rotatePhi(self.slider_rotate_x.value())

    def slider_changed_y(self):
        self.modelView.camera_controller.rotateTheta(self.slider_rotate_y.value())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

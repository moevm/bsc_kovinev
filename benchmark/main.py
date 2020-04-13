import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import benchmark.ui.add_software
import benchmark.ui.mainwindow
import benchmark.ui.model
import benchmark.ui.install_software_dialog

from benchmark.model.model3D import Model3D
from benchmark.panda3dwidget.ModelView import ModelView
from benchmark.panda3dwidget.PandaWidget import PandaWidget

from benchmark.utils.requeter import Requester
from benchmark.utils.unzipper import Unzipper
from benchmark.config.software import *
from benchmark.software.command_builder import CommandBuilder
from benchmark.utils.subprocessor import Subprocessor

class MainWindowApp(QtWidgets.QMainWindow, benchmark.ui.mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_buttons()
        self.init_configs()

    def init_buttons(self):
        self.actionAdd_Software.triggered.connect(self.f)
        self.actionAdd_Model.triggered.connect(self.add_model)
        self.actionInstall_Software.triggered.connect(self.install_software_dialog_call)
        self.actionCheck_exists.triggered.connect(self.check_exists)

    def add_model(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Model files (*.obj)")[0]
        print("[+] Filename passed from QFileDialog:", fname)
        if fname:
            m = Model3D(fname)
            widget = ModelWidget(self, m)
            self.layout_widgets.addWidget(widget)

    def f(self):
        dialog = AddSoftwareDialog(self)

    def install_software_dialog_call(self):
        dialog = InstallSoftwareDialog(self)

    def init_configs(self):
        self.configs = {
            "Meshroom": {
                "location": "/home/alien/Desktop/MeshroomMeshroom-2019.2.0-linux",
                "output": "/home/alien/Desktop/meshroom_output",
                "input": "/home/alien/Downloads/dataset_monstree-master/full/"
                }
            }


    def check_exists(self):
        print(self.configs["Meshroom"])
        builder = CommandBuilder(self.configs["Meshroom"])
        command = builder.buildStepViaConfig(ConfigSoftwareMeshroom.config, 0)
        print(command)
        def f(c):
            print(c)
        time = Subprocessor().run(command, callback=f)
        print(time)




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

        self.comboBox_select_default.addItems(["/home/alien/MEGA Syncs/diploma/models/house_red/zephyr/zephyr.obj",
                                               "/home/alien/MEGA Syncs/diploma/models/house_red/meshroom/texturedMesh.obj"])

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
        self.modelView = ModelView(model)
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


class InstallSoftwareDialog(QtWidgets.QDialog, benchmark.ui.install_software_dialog.Ui_Dialog):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)

        self.mainwindow = mainwindow

        self.init_buttons()

        self.show()
        self.exec_()

    def init_buttons(self):
        self.button_install.clicked.connect(self.install)

        self.comboBox.addItems(["Meshroom", "..."])
        self.comboBox_2.addItems(["/home/alien/Desktop/Meshroom", "..."])

    def close_dialog(self):
        self.close()

    def install(self):
        software = self.comboBox.currentText()
        dir = self.comboBox_2.currentText()
        if software == "Meshroom":
            s = ConfigSoftwareMeshroom.config
            url = s['settings']['install']['link']
            file = Requester.convert_url_to_file(url)

            self.label_status.setText(f"Download: {file}")
            file = Requester().get_file(s['settings']['install']['link'], dir=dir, callback=self.set_progress_bar)

            self.label_status.setText(f"Extracting: {file}")
            output = Unzipper().extract(file, callback=self.set_progress_bar)
            self.mainwindow.configs['Meshroom']["location"] = output

    def set_progress_bar(self, value):
        self.progress.setValue(value * 100)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import ui.add_software
import ui.mainwindow
import ui.model
import ui.install_software_dialog
import ui.comparison
from components.Table import TableModel
from meshlab.runner import MeshlabRunner

from model.model3D import Model3D
from panda3dwidget.ModelView import ModelView
from panda3dwidget.PandaWidget import PandaWidget

from utils.requeter import Requester
from utils.unzipper import Unzipper
from config.software import *
from software.command_builder import CommandBuilder
from utils.subprocessor import Subprocessor


class MainWindowApp(QtWidgets.QMainWindow, ui.mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_buttons()
        self.init_configs()

        self.list_of_models = []

    def init_buttons(self):
        self.actionAdd_Software.triggered.connect(self.f)
        self.actionAdd_Model.triggered.connect(self.add_model)
        self.actionInstall_Software.triggered.connect(self.install_software_dialog_call)
        self.actionCheck_exists.triggered.connect(self.check_exists)

    def add_model(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '~', "Model files (*.ply)")[0]
        if fname:
            m = Model3D(fname)
            widget = ModelWidget(self, m)
            self.layout_widgets.addWidget(widget)

            self.list_of_models.append(m)

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
        builder = CommandBuilder(self.configs["Meshroom"])
        command = builder.buildStepViaConfig(ConfigSoftwareMeshroom.config, 0)

        def f(c):
            print(c)

        time = Subprocessor().run(command, callback=f)
        print(time)


class AddSoftwareDialog(QtWidgets.QDialog, ui.add_software.Ui_Dialog):
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


class ModelWidget(QtWidgets.QWidget, ui.model.Ui_Form):
    def __init__(self, parent, model):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.model = model

        self.label_object_name.setText("Model: " + model.filename.split("/")[-1])
        self.modelView = ModelView(model)
        self.widget = PandaWidget(self.modelView, self.label_model_info)
        self.verticalLayout.addWidget(self.widget)

        self.init_buttons()

    def init_buttons(self):
        self.slider_rotate_x.valueChanged.connect(self.slider_changed_x)
        self.slider_rotate_y.valueChanged.connect(self.slider_changed_y)

        self.compare_button.clicked.connect(self.compare)

    def slider_changed_x(self):
        self.modelView.camera_controller.rotatePhi(self.slider_rotate_x.value())

    def slider_changed_y(self):
        self.modelView.camera_controller.rotateTheta(self.slider_rotate_y.value())

    def compare(self):
        dialog = CompareDialog(self, self.parent.list_of_models)


class InstallSoftwareDialog(QtWidgets.QDialog, ui.install_software_dialog.Ui_Dialog):
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


class CompareDialog(QtWidgets.QDialog, ui.comparison.Ui_Dialog):
    def __init__(self, model_widget, list_of_models):
        super().__init__()
        self.setupUi(self)

        self.model_widget = model_widget
        self.list_of_models = list_of_models

        self.comboBox_select.clear()
        self.comboBox_select.addItems(list(map(lambda x: x.short_filename, self.list_of_models)))

        self.compare_button.clicked.connect(self.compare)
        self.label_left.setText(self.model_widget.model.short_filename)

        self.show()
        self.exec_()

    def compare(self):
        clean_child(self.table_layout)
        clean_child(self.metrics_layout)

        current = self.model_widget.model

        selected = self.comboBox_select.currentText()
        second = list(filter(lambda x: x.short_filename == selected, self.list_of_models))[0]

        self.label_left.setText(current.short_filename)
        self.label_right.setText(second.short_filename)

        current_count_holes = MeshlabRunner().count_holes(current.filename)
        second_count_holes = MeshlabRunner().count_holes(current.filename)

        self.table_common = QtWidgets.QTableView()
        data = pd.DataFrame([
            [current.texture_memory, second.texture_memory],
            [current.vertices, second.vertices],
            [current.normals, second.normals],
            [current.tris, second.tris],
            [current_count_holes, second_count_holes],
        ], columns=[current.short_filename, second.short_filename],
            index=['Texture', 'Vertices', 'Normals', 'Tris', 'Count Holes'])

        self.table_common.setModel(TableModel(data))
        self.table_layout.addWidget(self.table_common)

        self.label_down.setText("Metrics:")

        metrics = MeshlabRunner().distance([current.filename, second.filename])

        self.table_metrics = QtWidgets.QTableView()
        data = pd.DataFrame([
            [metrics["min"]],
            [metrics["max"]],
            [metrics["mean"]],
            [metrics["RMS"]],
        ], columns=["Metric"],
            index=['Min', 'Max', 'Mean', 'RMS'])

        self.table_metrics.setModel(TableModel(data))
        self.table_layout.addWidget(self.table_metrics)


def clean_child(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import ui.comparison
import ui.mainwindow
import ui.model

from components.Table import TableModel
from meshlab.runner import MeshlabRunner
from model.model3D import Model3D
from panda3dwidget.ModelView import ModelView
from panda3dwidget.PandaWidget import PandaWidget


class MainWindowApp(QtWidgets.QMainWindow, ui.mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_buttons()

        self.list_of_models = []

    def init_buttons(self):
        self.actionAdd_Model.triggered.connect(self.add_model)

    def add_model(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '~', "Model files (*.ply)")[0]
        if fname:
            m = Model3D(fname)
            widget = ModelWidget(self, m)
            self.layout_widgets.addWidget(widget)

            self.list_of_models.append(m)


class ModelWidget(QtWidgets.QWidget, ui.model.Ui_Form):
    def __init__(self, parent, model):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.model = model

        self.label_object_name.setText("Model: " + model.short_filename)
        self.modelView = ModelView(model)
        self.widget = PandaWidget(self.modelView, self.label_model_info)
        self.verticalLayout.addWidget(self.widget)

        self.init_buttons()

    def init_buttons(self):
        self.slider_rotate_x.valueChanged.connect(self.slider_changed_x)
        self.slider_rotate_y.valueChanged.connect(self.slider_changed_y)
        self.slider_rotate_z.valueChanged.connect(self.slider_changed_z)

        self.compare_button.clicked.connect(self.compare)
        self.button_disable.clicked.connect(self.delete)

    def delete(self):
        self.parent.list_of_models.remove(self.model)
        clean_child(self.verticalLayout)
        clean_child(self.parent.layout_widgets)

    def slider_changed_x(self):
        self.modelView.camera_controller.rotatePhi(self.slider_rotate_x.value())

    def slider_changed_y(self):
        self.modelView.camera_controller.rotateTheta(self.slider_rotate_y.value())

    def slider_changed_z(self):
        self.modelView.camera_controller.rotateTheta(self.slider_rotate_z.value())

    def compare(self):
        dialog = CompareDialog(self, self.parent.list_of_models)


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

        output = MeshlabRunner().colorize([current.filename, second.filename])

        m = Model3D(output)
        widget = ModelWidget(self, m)
        clean_child(self.verticalLayout_2)
        self.verticalLayout_2.addWidget(widget)


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

import sys

import benchmark.ui.mainwindow
import benchmark.ui.add_software
import benchmark.ui.model

from PyQt5 import QtWidgets


class MainWindowApp(QtWidgets.QMainWindow, benchmark.ui.mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_buttons()

    def init_buttons(self):
        self.actionAdd_Software.triggered.connect(self.f)

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

    def close_dialog(self):
        self.close()

    def add_widget(self):
        widget = ModelWidget()
        self.mainwindow.layout_widgets.addWidget(widget)


class ModelWidget(QtWidgets.QWidget, benchmark.ui.model.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget_model.setStyleSheet("background-color:grey;")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

from PyQt5.QtCore import QSize, QSizeF, Qt
from PyQt5.QtGui import QImage, QPainter, QTransform
from PyQt5.QtWidgets import QWidget
from QPanda3D.QPanda3D_Keys_Translation import QPanda3D_Key_translation
from QPanda3D.QPanda3D_Modifiers_Translation import QPanda3D_Modifier_translation, QTimer
from direct.showbase.MessengerGlobal import messenger
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import Texture

from benchmark.utils.parsers import sceneGraphAnalyzerMeterParser


class QPanda3DSynchronizer(QTimer):
    def __init__(self, qPanda3DWidget, FPS=60):
        QTimer.__init__(self)
        self.qPanda3DWidget = qPanda3DWidget
        dt = 1000 / FPS
        self.setInterval(dt)
        self.timeout.connect(self.tick)

    def tick(self):
        taskMgr.step()
        self.qPanda3DWidget.update()


def get_panda_key_modifiers(evt):
    panda_mods = []
    qt_mods = evt.modifiers()
    for qt_mod, panda_mod in QPanda3D_Modifier_translation.items():
        if (qt_mods & qt_mod) == qt_mod:
            panda_mods.append(panda_mod)
    return panda_mods


def get_panda_key_modifiers_prefix(evt):
    # join all modifiers (except NoModifier, which is None) with '-'
    prefix = "-".join([mod for mod in get_panda_key_modifiers(evt) if mod is not None])

    # if the prefix is not empty, append a '-'
    if prefix:
        prefix += '-'

    return prefix


class PandaWidget(QWidget):
    def __init__(self, panda3DWorld, label_info, parent=None, FPS=60, debug=False):
        QWidget.__init__(self, parent)

        # set fixed geometry
        self.panda3DWorld = panda3DWorld
        self.panda3DWorld.set_parent(self)

        self.label_info = label_info

        self.setFocusPolicy(Qt.StrongFocus)
        self.paintSurface = QPainter()
        self.rotate = QTransform()
        self.rotate.rotate(180)
        self.out_image = QImage()

        size = self.panda3DWorld.cam.node().get_lens().get_film_size()
        self.initial_film_size = QSizeF(size.x, size.y)
        self.initial_size = self.size()

        self.synchronizer = QPanda3DSynchronizer(self, FPS)
        self.synchronizer.start()

        self.debug = debug

        self.update_sgam()

    def get_scene_graph_analyzer_meter(self):
        return self.panda3DWorld.get_scene_graph_analyzer_meter()

    def update_sgam(self):
        text = sceneGraphAnalyzerMeterParser(self.get_scene_graph_analyzer_meter()).toText()
        self.label_info.setText(text)

    def mousePressEvent(self, event):
        self.panda3DWorld.camera_controller.mouse_press(event.button(), event.x(), event.y())

    def mouseReleaseEvent(self, event):
        self.panda3DWorld.camera_controller.mouse_release(event.button(), event.x(), event.y())

    def mouseMoveEvent(self, event):
        self.panda3DWorld.camera_controller.mouse_move(event.button(), event.x(), event.y())

    def wheelEvent(self, evt):
        delta = -evt.angleDelta().y()
        self.panda3DWorld.camera_controller.zoom_event(delta)

    def keyPressEvent(self, evt):
        key = evt.key()
        try:
            k = "{}{}".format(get_panda_key_modifiers_prefix(evt), QPanda3D_Key_translation[key])
            if self.debug:
                print(k)
            messenger.send(k)
        except:
            print("Unimplemented key. Please send an issue on github to fix this problem")

    def keyReleaseEvent(self, evt):
        key = evt.key()
        try:
            k = "{}{}-up".format(get_panda_key_modifiers_prefix(evt), QPanda3D_Key_translation[key])
            if self.debug:
                print(k)
            messenger.send(k)
        except:
            print("Unimplemented key. Please send an issue on github to fix this problem")

    def resizeEvent(self, evt):
        lens = self.panda3DWorld.cam.node().get_lens()
        lens.set_film_size(self.initial_film_size.width() * evt.size().width() / self.initial_size.width(),
                           self.initial_film_size.height() * evt.size().height() / self.initial_size.height())
        self.panda3DWorld.buff.setSize(evt.size().width(), evt.size().height())

    def minimumSizeHint(self):
        return QSize(400, 300)

    # Use the paint event to pull the contents of the panda texture to the widget
    def paintEvent(self, event):
        if self.panda3DWorld.screenTexture.mightHaveRamImage():
            self.panda3DWorld.screenTexture.setFormat(Texture.FRgba32)
            data = self.panda3DWorld.screenTexture.getRamImage().getData()
            img = QImage(data, self.panda3DWorld.screenTexture.getXSize(), self.panda3DWorld.screenTexture.getYSize(),
                         QImage.Format_ARGB32).mirrored()
            self.paintSurface.begin(self)
            self.paintSurface.drawImage(0, 0, img)

            self.paintSurface.end()

    def rotateX(self, value):
        self.panda3DWorld.camera_controller.rotateTheta(value)

    def rotateY(self, value):
        self.panda3DWorld.camera_controller.rotatePhi(value)

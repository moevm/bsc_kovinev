import math

from PyQt5.QtCore import Qt
from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, Point3, Vec3


class CameraController(DirectObject):
    def __init__(self, base, r, theta, phi):
        DirectObject.__init__(self)
        self.base = base

        # Parameters
        self.rotateMag = 0.5
        self.moveMag = 50
        self.zoomMag = 15

        # Camera properties
        self.r = r
        self.theta = theta
        self.phi = phi

        self.target = NodePath("target")
        self.target.reparentTo(self.base.render)
        self.base.camera.reparentTo(self.target)

        # Controls
        self.mouseDown1 = False
        self.mouseDown2 = False
        self.mouseDown3 = False
        self.mousePrevX = 0.0
        self.mousePrevY = 0.0

        self.updateCamera(0, 0)

    def setTarget(self, parent):
        self.target.reparentTo(parent)

    def rotateTheta(self, value):
        self._rotateTheta(value)
        self.updateCamera(self.mousePrevX, self.mousePrevY)

    def rotatePhi(self, value):
        self._rotatePhi_for_scroll(math.radians(value))
        self.updateCamera(self.mousePrevX, self.mousePrevY)

    def mouse_press(self, button, x, y):
        self.mouseDown1 = True if button == Qt.LeftButton else self.mouseDown1
        self.mouseDown2 = True if button == Qt.RightButton else self.mouseDown2
        self.mouseDown3 = True if button == Qt.MiddleButton else self.mouseDown3

        self.mousePrevX = x
        self.mousePrevY = y

        self.updateCamera(x, y)

    def mouse_release(self, button, x, y):
        self.mouseDown1 = False if button == Qt.LeftButton else self.mouseDown1
        self.mouseDown2 = False if button == Qt.RightButton else self.mouseDown2
        self.mouseDown3 = False if button == Qt.MiddleButton else self.mouseDown3

        self.mousePrevX = x
        self.mousePrevY = y

    def mouse_move(self, button, x, y):
        self.updateCamera(x, y)

    def zoom_event(self, delta):
        self.zoom(delta)
        self.updateCamera(self.mousePrevX, self.mousePrevY)

    def updateCamera(self, x, y):
        factor = 0.01
        dX = (self.mousePrevX - x) * factor
        dY = (self.mousePrevY - y) * factor

        if self.mouseDown1:
            self._rotateTheta(dX * math.pi * self.rotateMag)
            self._rotatePhi(-dY * math.pi * self.rotateMag)

        if self.mouseDown2:
            vecX = self.target.getRelativeVector(self.base.camera, Vec3.right())
            vecY = self.target.getRelativeVector(self.base.camera, Vec3.forward())
            vecY.setZ(0.0)
            vecY.normalize()
            offset = (vecX * dX * self.moveMag) + (vecY * dY * self.moveMag)
            self.target.setPos(self.target, offset)

        if self.mouseDown3:
            self.zoom(dY * self.zoomMag)

        self.mousePrevX = x
        self.mousePrevY = y

        # Update camera position
        position = Point3(0.0, 0.0, 0.0)
        position.setX(self.r * math.cos(self.theta) * math.sin(self.phi))
        position.setY(self.r * math.sin(self.theta) * math.sin(self.phi))
        position.setZ(self.r * math.cos(self.phi))
        self.base.camera.setPos(position)
        self.base.camera.lookAt(self.target)

    def zoom(self, delta):
        self.r += delta * 0.2
        if self.r < 0.0:
            self.r = 0.0

    def _rotateTheta(self, dTheta):
        self.theta += dTheta
        if self.theta < 0.0:
            self.theta += 2 * math.pi
        if self.theta > 2 * math.pi:
            self.theta -= 2 * math.pi

    def _rotatePhi(self, dPhi):
        self.phi += dPhi
        if self.phi < 0.1:
            self.phi = 0.1
        if self.phi > math.pi - 0.1:
            self.phi = math.pi - 0.1


    def _rotatePhi_for_scroll(self, dPhi):
        self.phi += dPhi
        if self.phi < 0.1:
            self.phi = 0.1
        if self.phi > math.pi - 0.1:
            self.phi = self.phi - math.pi

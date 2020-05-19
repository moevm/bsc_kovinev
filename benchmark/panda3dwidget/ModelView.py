import math

from QPanda3D.Helpers.Env_Grid_Maker import *
from QPanda3D.Panda3DWorld import Panda3DWorld

from panda3dwidget.CameraController import CameraController


class ModelView(Panda3DWorld):
    def __init__(self, model3D):
        self.model3D = model3D

        Panda3DWorld.__init__(self)
        self.disable_mouse()

        self.camera_controller_ = CameraController(self, 600, math.radians(45), math.radians(60))

        self.set_collisions_handlers()
        self.set_light()
        self.draw_model(self.model3D.filename)
        #self.draw_grid()

        self.setFrameRateMeter(True)
        self.setSceneGraphAnalyzerMeter(True)

        self.model3D.set_sgam(self.get_scene_graph_analyzer_meter())

    @property
    def camera_controller(self):
        return self.camera_controller_

    def set_collisions_handlers(self):
        # Collision traverser
        self.cTrav = CollisionTraverser("collisionTraverser")

        # Collision handlers
        self.carCollisionHandler = CollisionHandlerEvent()
        self.carCollisionHandler.addInPattern("%fn-into-%in")

    def set_light(self):
        # Lights
        alight = AmbientLight("alight")
        alnp = self.render.attachNewNode(alight)
        alight.setColor(VBase4(0.8, 0.8, 0.8, 0))
        self.render.setLight(alnp)

    def draw_model(self, path_model):
        self.model = self.loader.loadModel(path_model)
        self.model.setPos(0, 0, 0)
        # self.model.setLightOff()
        self.model.reparentTo(self.render)

    def draw_grid(self):
        self.grid_maker = Env_Grid_Maker()
        self.grid = self.grid_maker.create()
        self.grid.reparentTo(self.render)
        self.grid.setLightOff()

    def get_scene_graph_analyzer_meter(self):
        return self.sceneGraphAnalyzerMeter

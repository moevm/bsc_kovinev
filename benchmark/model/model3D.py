class Model3D:
    def __init__(self, filename=""):
        self.filename_ = filename
        self.mesh = []
        self.vertices_ = 0
        self.normals_ = 0
        self.tris_ = 0
        self.texture_memory_ = ""

    @property
    def filename(self):
        return self.filename_

    def set_sgam(self, sgam):
        sgam_dict = sgam.toDict()
        self.texture_ = sgam_dict["Texture"]
        self.vertices_ = sgam_dict["Vertices"]
        self.normals_ = sgam_dict["Normals"]
        self.tris_ = sgam_dict["Tris"]

    @property
    def vertices(self):
        return self.vertices_

    @property
    def normals(self):
        return self.normals_

    @property
    def tris(self):
        return self.tris_

    @property
    def texture_memory(self):
        return self.texture_

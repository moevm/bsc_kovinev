import re


class Model3D:
    """
        Class Model3D
        Contains main information about generated or imorted models
        @param filename: path to the file with the model (.obj)
    """
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
        sgam = str(sgam)
        regex_texture = re.compile(r"Texture memory: ([\d\.]+)")
        regex_vertices = re.compile(r"Vertices: (\d+)")
        regex_normals = re.compile(r"Normals: (\d+)")
        regex_tris = re.compile(r"Tris: (\d+)")

        self.texture_memory_ = re.findall(regex_texture, sgam)[0]
        self.vertices_ = re.findall(regex_vertices, sgam)[0]
        self.normals_ = re.findall(regex_normals, sgam)[0]
        self.tris_ = re.findall(regex_tris, sgam)[0]

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

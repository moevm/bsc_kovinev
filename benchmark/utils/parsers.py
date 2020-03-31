import re


class sceneGraphAnalyzerMeterParser:
    def __init__(self, sceneGraphAnalyzerMeter):
        self.sgam = sceneGraphAnalyzerMeter
        self.vertices_ = 0
        self.normals_ = 0
        self.tris_ = 0
        self.texture_memory_ = ""

        self._parse()

    def _parse(self):
        regex_v = re.compile("Vertices: ([\d]+)")
        regex_n = re.compile("Normals: ([\d]+)")
        regex_t = re.compile("Tris: ([\d]+)")
        regex_m = re.compile("Texture memory: (.*B)")

        self.vertices_ = re.findall(regex_v, str(self.sgam))[0]
        self.normals_ = re.findall(regex_n, str(self.sgam))[0]
        self.tris_ = re.findall(regex_t, str(self.sgam))[0]
        self.texture_memory_ = re.findall(regex_m, str(self.sgam))[0]

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
        return self.texture_memory_

    def toText(self):
        return f"Texture: {self.texture_memory}\n" \
               f"Vertices: {self.vertices}\n" \
               f"Normals: {self.normals}\n" \
               f"Tris: {self.tris}"

    def toDict(self):
        return {"Texture": self.texture_memory,
                "Vertices": self.vertices,
                "Normals": self.normals,
                "Tris": self.tris}

    def __str__(self):
        return self.toText()
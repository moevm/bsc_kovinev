class Model3D:
    def __init__(self, filename=""):
        self.filename_ = filename
        self.mesh = []

    @property
    def filename(self):
        return self.filename_


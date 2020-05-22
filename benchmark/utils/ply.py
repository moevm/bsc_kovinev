import meshio

from utils.d3.model import tools as mt


class ConvertToPly:
    def __init__(self, file):
        self.output = self.generete_name(file)
        self.save_as_ply(file)

    def save_as_ply(self, file):
        mesh = meshio.read(file)
        mesh.write(self.output)

    def generete_name(self, file):
        return file.replace('.obj', '.ply')

    def name(self):
        return self.output
from utils.d3.model import tools as mt


class ConvertToPly:
    def __init__(self, file):
        self.output = self.generete_name(file)
        result = mt.convert(file, self.output, None)

        with open(self.output, 'w') as f:
            f.write(result)


    def generete_name(self, file):
        return file.replace('.obj', '.ply')

    def name(self):
        return self.output
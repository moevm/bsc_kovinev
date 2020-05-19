import os
import pathlib
import re

import sys

from utils.ply import ConvertToPly

sys.path.extend(['.', '..', '../..'])
from utils.subprocessor import Subprocessor


class MeshlabRunner:
    def __init__(self):
        self._count = 0
        self._distance = ''
        self.stop = False

    def _callback_holes(self, input):
        regex = re.compile(r"(\d+) holes")
        res = re.findall(regex, input["output"])
        if res:
            self._count = res[0]

    def _callback_distance(self, input):
        regex = re.compile(r"min : ([\d,]+)\s+max ([\d,]+)\s+mean : ([\d,]+)\s+RMS : ([\d,]+)")
        res = re.findall(regex, input["output"])
        if res and not self.stop:
            self._distance = {
                "min": self._toFloat(res[0][0]),
                "max": self._toFloat(res[0][1]),
                "mean": self._toFloat(res[0][2]),
                "RMS": self._toFloat(res[0][3]),
            }
            self.stop = True

    @staticmethod
    def _toFloat(v):
        return float(v.replace(',', '.'))

    def build_command(self, input=[], output=[], type=None):
        cmd = "meshlabserver "
        for obj in input:
            cmd += f"-i {obj} "

        for obj in output:
            cmd += f"-o {obj} "

        path = str(pathlib.Path(__file__).parent.absolute()) + "/configurations"

        if type == "HOLES":
            cmd += f" -s {path}/holes.mlx"
        elif type == "DISTANCE":
            cmd += f" -s {path}/distance.mlx"
        elif type == "COLORIZE":
            cmd += f" -om vc vn vt fc wt -s {path}/colorize.mlx"

        print(cmd)
        return cmd

    def count_holes(self, obj):
        cmd = self.build_command(input=[obj], type="HOLES")
        Subprocessor().run(cmd, self._callback_holes)
        return self._count

    def distance(self, objs):
        cmd = self.build_command(input=objs, type="DISTANCE")
        Subprocessor().run(cmd, self._callback_distance)
        return self._distance

    def colorize(self, objs):
        #objs = [ConvertToPly(o).name() for o in objs]
        output = self.generate_temp_file()
        cmd = self.build_command(input=objs, output=[output], type="COLORIZE")

        Subprocessor().run(cmd)
        return output

    def generate_temp_file(self):
        DIR = "./temp_models"
        if not os.path.exists(DIR):
            os.makedirs(DIR)
        return f"{DIR}/{self.random_string()}"

    def random_string(self):
        import string, random
        return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)]) + '.ply'




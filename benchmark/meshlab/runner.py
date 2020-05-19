import pathlib
import re

import sys
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
        return cmd

    def count_holes(self, obj):
        cmd = self.build_command(input=[obj], type="HOLES")
        Subprocessor().run(cmd, self._callback_holes)
        return self._count

    def distance(self, objs):
        cmd = self.build_command(input=objs, type="DISTANCE")
        Subprocessor().run(cmd, self._callback_distance)
        return self._distance





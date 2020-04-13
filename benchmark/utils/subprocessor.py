import subprocess
import time

class STD_STATUS:
    STDOUT = "stdout"
    STDERR = "stderr"


class Subprocessor:
    def __init__(self):
        pass

    @staticmethod
    def decode_output(output):
        return output.strip().decode('utf-8')

    def run(self, command, callback=None):
        start = time.time()
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        while True:
            stdoutput = process.stdout.readline()
            stderrput = process.stderr.readline()

            if stdoutput.decode('utf-8') == '' and process.poll() is not None:
                break

            if stdoutput and callback:
                callback({"STD_STATUS": STD_STATUS.STDOUT, "output": self.decode_output(stdoutput)})

            if stderrput and callback:
                callback({"STD_STATUS": STD_STATUS.STDERR, "output": self.decode_output(stderrput)})

        process.poll()

        end = time.time()
        return end - start
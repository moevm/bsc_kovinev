import os
import re


class CommandBuilder:
    def __init__(self, config=None):
        self.config = {
            "location": "/home/alien/Software/git/Meshroom-2019.2.0",
            "output": "/home/alien/Desktop/meshroom_output",
            "input": "/home/alien/Downloads/dataset_monstree-master/full/"
        } if not config else config

    @staticmethod
    def makeDir(path):
        try:
            os.system(f"mkdir -p {path}")
        except:
            pass
        return 0

    def createSubDir(self, path, is_folder):
        print(path)
        if is_folder:
            self.makeDir(path)
        else:
            regex = re.compile(r"(.*\/).*")
            self.makeDir(re.findall(regex, path)[0])

    def buildStepViaConfig(self, config_software, step, specific_params=None):
        run_commands = config_software["settings"]["run"]

        environ_params = run_commands["environ"]
        for param in environ_params:
            key = list(param.keys())[0]
            if not param[key]["is_path"]:
                key, value = param[key]["key"], param[key]["value"]
            else:
                key, value = param[key]["key"], f'{self.config["location"]}{config_software["settings"]["run"]["directory"]}/{param[key]["value"]}'

            os.environ[key] = value

        is_step_running_support = run_commands["is_step_running_support"]

        if not is_step_running_support:
            return  # TODO exception

        steps_count = run_commands["steps"]["steps_count"]
        if step > steps_count:
            return  # TODO exception

        step = run_commands["steps"]["steps"][step][step]

        exe = f'{self.config["location"]}{config_software["settings"]["run"]["directory"]}{step["executable_dir"]}{step["executable"]} '

        if not step["output"]["is_output_required"]:
            output_args = ""
        else:
            output_path = f'{self.config["output"]}{step["output"]["output_location"]}'
            output_args = f'{step["output"]["output_key"]} {output_path} '
            self.createSubDir(output_path, step["output"]["output_is_folder"])

        if not step["input"]["is_input_required"]:
            input_args = ""
        else:
            input_args = f'{step["input"]["input_key"]} {self.config["output"]}{step["input"]["input_location"]} '

        if not step["images"]["is_image_required"]:
            images_args = ""
        else:
            images_args = f'{step["images"]["input_image_key"]} {self.config["input"]} '

        extra_args = step["extra_args"] + ' '
        specific_args = step["specific_args"].format(specific_params) if specific_params else step["specific_args"]

        args = output_args + input_args + images_args + extra_args + specific_args
        return exe + args

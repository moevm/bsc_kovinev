from benchmark.utils.readers.yaml_reader import YAML_Reader

class ConfigSoftware:
    link = ""
    install_command = ""


class ConfigSoftwareMeshroom(ConfigSoftware):
    # TODO fix path
    config_path = '/home/alien/Desktop/git/bsc_kovinev/benchmark/config/yaml/meshroom.yaml'
    config = YAML_Reader.read(config_path)




from utils.readers.yaml_reader import YAML_Reader

class ConfigSoftware:
    link = ""
    install_command = ""


class ConfigSoftwareMeshroom(ConfigSoftware):
    config_path = './config/yaml/meshroom.yaml'
    config = YAML_Reader.read(config_path)




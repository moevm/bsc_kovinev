import yaml


class YAML_Reader:
    @staticmethod
    def read(file):
        with open(file, "r") as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    @staticmethod
    def write(file, data):
        with open(file, "w", encoding="utf-8") as f:
            f.write(yaml.dump(data, default_flow_style=False))

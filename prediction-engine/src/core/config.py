import yaml

class Config:
    def __init__(self, config_file="config/settings.yaml"):
        with open(config_file, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self, key):
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k)
        return value

config = Config()

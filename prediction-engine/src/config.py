import os
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")


def load_config(config_path=CONFIG_PATH):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


CONFIG = load_config()

# Access parameters
MODEL_PATH = os.path.join(BASE_DIR, CONFIG['paths']['model'])
DATASET_PATH = os.path.join(BASE_DIR, CONFIG['paths']['dataset'])
LOG_FILE = os.path.join(BASE_DIR, CONFIG['paths']['logs'])
BATCH_SIZE = CONFIG['training']['batch_size']
EPOCHS = CONFIG['training']['epochs']
LEARNING_RATE = CONFIG['training']['learning_rate']
API_HOST = CONFIG['api']['host']
API_PORT = CONFIG['api']['port']

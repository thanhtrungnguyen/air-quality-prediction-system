import logging
import logging.config
import yaml

# Load logging configuration from YAML
with open("config/logging.yaml", "r") as f:
	logging_config = yaml.safe_load(f)
logging.config.dictConfig(logging_config)

# Get logger instance
logger = logging.getLogger("prediction_engine")

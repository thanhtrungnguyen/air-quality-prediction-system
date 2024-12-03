import tensorflow as tf
from src.core.config import config
from src.core.logger import logger

def load_model():
    """
    Load the TensorFlow model from the specified path.
    """
    model_path = config.get("model.path")
    logger.info("Loading model from %s", model_path)
    try:
        model = tf.keras.models.load_model(model_path)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error("Failed to load model: %s", str(e))
        raise

import os
import tensorflow as tf

def save_model(model, path):
    """
    Save a TensorFlow model to the specified path.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    model.save(path)
    print(f"Model saved to {path}")

def load_model(path):
    """
    Load a TensorFlow model from the specified path.
    """
    if os.path.exists(path):
        print(f"Loading model from {path}")
        return tf.keras.models.load_model(path)
    else:
        raise FileNotFoundError(f"No model found at {path}")

def print_summary(model):
    """
    Print a summary of the TensorFlow model.
    """
    model.summary()

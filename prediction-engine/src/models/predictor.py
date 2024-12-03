import numpy as np
from src.models.loader import load_model

model = load_model()

def make_prediction(input_data):
    """
    Generate a prediction using the TensorFlow model.
    """
    features = np.array([[input_data.temperature, input_data.humidity, input_data.traffic_density]])
    prediction = model.predict(features)
    return float(prediction[0][0])

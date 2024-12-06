import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from src.config import MODEL_PATH  # Define target variable names

TARGET_COLUMNS = ["CO", "NO", "NO2", "O3", "SO2", "PM2_5", "PM10", "NH3", "AQI"]


def predict(input_data: pd.DataFrame) -> pd.DataFrame:
    """
    Predict air quality metrics given input features.
    :param input_data: Input data as a Pandas DataFrame.
    :return: Pandas DataFrame containing predictions with field names.
    """
    model = tf.keras.models.load_model(MODEL_PATH)

    # Preprocess input data (e.g., scaling)
    input_scaled = input_data.values  # Example, ensure this matches your scaler's requirements

    # Get predictions
    predictions = model.predict(input_scaled)

    # Convert predictions to DataFrame with field names
    predictions_df = pd.DataFrame(predictions, columns=TARGET_COLUMNS)

    return predictions_df

import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler

def evaluate_model(model_path, data_file):
    """
    Evaluate a TensorFlow model on a dataset.
    """
    # Load the data
    data = pd.read_csv(data_file)
    X = data[['temperature', 'humidity', 'traffic_density']].values
    y = data['pm25'].values

    # Normalize features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Load the model
    model = tf.keras.models.load_model(model_path)

    # Evaluate the model
    loss, mae = model.evaluate(X, y)
    print(f"Loss: {loss}, Mean Absolute Error: {mae}")

# Example usage
if __name__ == "__main__":
    evaluate_model("../models/air_quality_model", "../data/processed/training_data.csv")

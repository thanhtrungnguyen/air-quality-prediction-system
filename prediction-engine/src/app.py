from flask import Flask, request, jsonify
import pandas as pd
from pydantic import ValidationError

from src.models.predict_model import predict
from typing import Dict, Any
from config import API_HOST, API_PORT
from src.preprocess import consolidate_weather_description
from src.schemas.input_schema import PredictionInput
from src.schemas.output_schema import PredictionOutput

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify API status.
    """
    return jsonify({"status": "healthy", "message": "API is running successfully!"}), 200


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    """
    API endpoint for making predictions based on input features.
    """
    try:
        # Parse JSON input
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input to DataFrame
        input_df = pd.DataFrame([data])

        # Preprocess weather description
        input_df = consolidate_weather_description(input_df)

        # Validate the preprocessed input
        validated_input = PredictionInput(**input_df.to_dict(orient="records")[0])

        # Call the prediction function
        predictions_df = predict(pd.DataFrame([validated_input.dict()]))

        # Convert predictions to output schema
        predictions_dict = predictions_df.to_dict(orient="records")[0]
        output = PredictionOutput(
            predictions=predictions_dict,
            message="Prediction successful"
        )

        return jsonify(output.dict()), 200

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

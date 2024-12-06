from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class PredictionOutput(BaseModel):
    """
    Defines the updated output schema for the prediction API.
    """
    predictions: Dict[str, float] = Field(
        ...,
        description="Predicted air quality metrics with target names as keys and values as predictions"
    )
    message: str = Field(
        ...,
        description="Message about the API response",
        example="Prediction successful"
    )

    class Config:
        schema_extra = {
            "example": {
                "predictions": {
                    "CO": 0.25,
                    "NO": 0.03,
                    "NO2": 0.1,
                    "O3": 0.05,
                    "SO2": 0.02,
                    "PM2_5": 0.5,
                    "PM10": 0.4,
                    "NH3": 0.03,
                    "AQI": 50
                },
                "message": "Prediction successful"
            }
        }


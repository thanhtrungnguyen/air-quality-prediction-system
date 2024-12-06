from pydantic import BaseModel, Field
from typing import Optional


class PredictionInput(BaseModel):
    """
    Defines the input schema for the prediction API.
    """
    temperature_c: float = Field(..., description="Temperature in Celsius", example=25.0)
    feels_like_c: float = Field(..., description="Temperature in Celsius", example=25.0)
    pressure_hpa: float = Field(..., description="Pressure in hPa", example=1013.25)
    humidity_percent: float = Field(..., description="Humidity percentage", example=60.0)
    wind_speed_m_s: float = Field(..., description="Wind speed in m/s", example=5.0)
    wind_direction_deg: float = Field(..., description="Wind direction in degrees", example=270.0)
    cloudiness_percent: float = Field(..., description="Cloudiness percentage", example=75.0)
    weather_description: str = Field(..., description="Description of the weather", example="Cloudy")
    additional_feature: Optional[float] = Field(None, description="Optional additional feature")

    class Config:
        schema_extra = {
            "example": {
                "temperature": 25.0,
                "humidity": 60.0,
                "wind_speed": 5.0
            }
        }

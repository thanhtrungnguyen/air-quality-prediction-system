from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    temperature: float = Field(..., ge=-50, le=50, description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Humidity percentage")
    traffic_density: float = Field(..., ge=0, le=100, description="Traffic density index")

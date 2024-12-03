from fastapi import APIRouter
from src.api.schemas import PredictionInput
from src.models.predictor import make_prediction

router = APIRouter()

@router.post("/predict", summary="Predict PM2.5 Levels")
async def predict(input_data: PredictionInput):
    """
    Predict PM2.5 levels based on temperature, humidity, and traffic density.
    """
    prediction = make_prediction(input_data)
    return {"pm25_prediction": prediction}

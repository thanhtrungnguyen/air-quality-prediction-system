from fastapi import FastAPI
from src.api.routes import router as api_router
from src.config import config
from src.core.logger import logger

# Initialize FastAPI app
app = FastAPI(
    title="Prediction Engine",
    description="A REST API for air quality prediction using TensorFlow",
    version="1.0.0"
)

# Include API routes
app.include_router(api_router)


# Event handlers for startup and shutdown
@app.on_event("startup")
async def startup_event():
    logger.info("Prediction Engine is starting...")
    # Add any initialization logic here
    logger.info("Configuration Loaded: %s", config.config)


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Prediction Engine is shutting down...")




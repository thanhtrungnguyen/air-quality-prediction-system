from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Stub Data
summary_stub = {
    "date": "2020-11-25",
    "AQI": 154,
    "status": "Unhealthy",
    "levels": {
        "co": 2162.93,
        "no": 0.00,
        "no2": 58.95,
        "o3": 72.96,
        "so2": 95.37,
        "pm2_5": 346.73,
        "pm10": 385.34,
        "nh3": 9.37,
    },
}

forecast_stub = [
    {
        "date": "2020-11-25",
        "AQI": 154,
        "status": "Unhealthy",
        "temp": "22° - 19°",
        "wind": "7.2 km/h",
    },
    {
        "date": "2020-11-26",
        "AQI": 136,
        "status": "Moderate",
        "temp": "24° - 21°",
        "wind": "10.8 km/h",
    },
    {
        "date": "2020-11-27",
        "AQI": 161,
        "status": "Unhealthy",
        "temp": "26° - 22°",
        "wind": "14.4 km/h",
    },
]

# Routes
@app.route("/api/summary", methods=["GET"])
def get_summary():
    """Return air quality summary data."""
    return jsonify(summary_stub)

@app.route("/api/forecast", methods=["GET"])
def get_forecast():
    """Return air quality forecast data."""
    return jsonify(forecast_stub)

if __name__ == "__main__":
    app.run(debug=True)

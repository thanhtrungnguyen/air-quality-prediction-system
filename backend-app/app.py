import time
import requests
import psycopg2
from psycopg2 import sql
from datetime import datetime

DB_CONFIG = {
    "dbname": "weather_service",
    "user": "your_db_user",  # Replace with your PostgreSQL username
    "password": "your_db_password",  # Replace with your PostgreSQL password
    "host": "localhost",
    "port": "5432"
}

FIRST_API_URL = "http://api.openweathermap.org/data/2.5/forecast"
SECOND_API_URL = "https://example.com/api/predict"
API_KEY = "bd5e378503939ddaee76f12ad7a97608"
CITY = "Hanoi"

# Service 1: Fetch data from the first API and save to the database
def fetch_weather_data():
    params = {"q": CITY, "appid": API_KEY, "units": "metric"}
    response = requests.get(FIRST_API_URL, params=params)
    response.raise_for_status()
    return response.json()

def parse_weather_data(data):
    city = data["city"]["name"]
    country = data["city"]["country"]
    forecasts = []

    for entry in data["list"]:
        forecast_time = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
        temperature = entry["main"]["temp"]
        feels_like = entry["main"]["feels_like"]
        pressure = entry["main"]["pressure"]
        humidity = entry["main"]["humidity"]
        wind_speed = entry["wind"]["speed"]
        wind_direction = entry["wind"]["deg"]
        cloudiness = entry["clouds"]["all"]
        weather_description = entry["weather"][0]["description"]

        forecasts.append({
            "city": city,
            "country": country,
            "forecast_time": forecast_time,
            "temperature": temperature,
            "feels_like": feels_like,
            "pressure": pressure,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
            "cloudiness": cloudiness,
            "weather_description": weather_description,
            "timestamp": None,
            "CO": None,
            "NO": None,
            "NO2": None,
            "O3": None,
            "SO2": None,
            "PM2_5": None,
            "PM10": None,
            "NH3": None,
            "AQI": None
        })

    return forecasts

def save_to_database(forecasts):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        insert_query = sql.SQL("""
            INSERT INTO weather_forecast (
                city, country, forecast_time, temperature, feels_like,
                pressure, humidity, wind_speed, wind_direction,
                cloudiness, weather_description, timestamp, CO, NO, NO2,
                O3, SO2, PM2_5, PM10, NH3, AQI
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)

        for forecast in forecasts:
            cursor.execute(insert_query, (
                forecast["city"],
                forecast["country"],
                forecast["forecast_time"],
                forecast["temperature"],
                forecast["feels_like"],
                forecast["pressure"],
                forecast["humidity"],
                forecast["wind_speed"],
                forecast["wind_direction"],
                forecast["cloudiness"],
                forecast["weather_description"],
                forecast["timestamp"],
                forecast["CO"],
                forecast["NO"],
                forecast["NO2"],
                forecast["O3"],
                forecast["SO2"],
                forecast["PM2_5"],
                forecast["PM10"],
                forecast["NH3"],
                forecast["AQI"]
            ))

        conn.commit()
        print(f"Inserted {len(forecasts)} rows into the database.")
    except Exception as e:
        print(f"Error saving to database: {e}")
    finally:
        cursor.close()
        conn.close()

def run_first_service():
    print("Fetching weather data...")
    data = fetch_weather_data()
    print("Parsing weather data...")
    forecasts = parse_weather_data(data)
    print("Saving weather data to the database...")
    save_to_database(forecasts)
    print("First service completed.")

# Service 2: Call the second API with DB entries and update predictions
def fetch_unprocessed_entry():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM weather_forecast
            WHERE CO IS NULL
            LIMIT 1;
        """)

        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            columns = [desc[0] for desc in cursor.description]
            entry = dict(zip(columns, row))
            return entry
        return None

    except Exception as e:
        print(f"Error fetching entry: {e}")
    finally:
        cursor.close()
        conn.close()

def call_prediction_api(entry):
    try:
        payload = {"entry": entry}  # You may structure this as required by the second API
        response = requests.post(SECOND_API_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error calling prediction API: {e}")
        return None

def update_entry_with_predictions(entry_id, predictions):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        update_query = sql.SQL("""
            UPDATE weather_forecast
            SET CO = %s, NO = %s, NO2 = %s, O3 = %s, SO2 = %s,
                PM2_5 = %s, PM10 = %s, NH3 = %s, AQI = %s
            WHERE id = %s;
        """)

        cursor.execute(update_query, (
            predictions["CO"],
            predictions["NO"],
            predictions["NO2"],
            predictions["O3"],
            predictions["SO2"],
            predictions["PM2_5"],
            predictions["PM10"],
            predictions["NH3"],
            predictions["AQI"],
            entry_id
        ))

        conn.commit()
        print(f"Updated entry ID {entry_id} with predictions.")
    except Exception as e:
        print(f"Error updating entry: {e}")
    finally:
        cursor.close()
        conn.close()

def main_service_loop():
    while True:
        entry = fetch_unprocessed_entry()
        if entry:
            print(f"Processing entry ID {entry['id']}...")
            predictions = call_prediction_api(entry)
            if predictions and "predictions" in predictions:
                update_entry_with_predictions(entry["id"], predictions["predictions"])
            else:
                print("Failed to get valid predictions.")
        else:
            print("No unprocessed entries. Running first service...")
            run_first_service()
            print("Pausing for 30 minutes...")
            time.sleep(1800)

if __name__ == "__main__":
    main_service_loop()

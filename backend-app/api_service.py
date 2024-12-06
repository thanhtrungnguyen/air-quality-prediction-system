from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from datetime import datetime, timedelta

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "weather_service",
    "user": "your_db_user",  # Replace with your PostgreSQL username
    "password": "your_db_password",  # Replace with your PostgreSQL password
    "host": "localhost",
    "port": "5432"
}

# Database connection utility
def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

# Endpoint: Get weather data for the next 5 days
@app.route('/next-5-days', methods=['GET'])
def next_5_days():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM weather_forecast
            WHERE forecast_time BETWEEN NOW() AND NOW() + INTERVAL '5 days';
        """)

        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert rows to dictionary
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]

        return jsonify({"status": "success", "data": data})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    finally:
        cursor.close()
        conn.close()

# Endpoint: Get weather data for a specific date
@app.route('/by-date', methods=['POST'])
def by_date():
    try:
        # Parse date from request body
        req_data = request.get_json()
        date_str = req_data.get("date")
        if not date_str:
            return jsonify({"status": "error", "message": "Date is required."})

        # Convert to datetime object
        date = datetime.strptime(date_str, "%Y-%m-%d")

        conn = get_db_connection()
        cursor = conn.cursor()

        query = sql.SQL("""
            SELECT * FROM weather_forecast
            WHERE forecast_time::date = %s;
        """)

        cursor.execute(query, (date,))
        rows = cursor.fetchall()

        # Convert rows to dictionary
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]

        return jsonify({"status": "success", "data": data})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    finally:
        cursor.close()
        conn.close()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

import configparser
import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

DB_NAME = "config_data.db"

def parse_config(file_path: str) -> dict:
    """
    Parse configuration file and return dictionary of sections and key-value pairs.
    """
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        if not config.sections():
            raise FileNotFoundError("Configuration file is empty or not found.")

        config_dict = {section: dict(config.items(section)) for section in config.sections()}
        return config_dict
    except Exception as e:
        print(f"⚠️ Error reading configuration file: {e}")
        return {}


def save_to_db(data: dict):
    """
    Save JSON data into SQLite database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS config_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL
            )
        """)

        # Insert JSON data
        cursor.execute("INSERT INTO config_data (data) VALUES (?)", (json.dumps(data),))
        conn.commit()
        conn.close()
        print("✅ Configuration data saved to database successfully.")
    except Exception as e:
        print(f"⚠️ Error saving to database: {e}")


@app.route('/get_config', methods=['GET'])
def get_config():
    """
    GET endpoint to fetch configuration data from database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT data FROM config_data ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify(json.loads(row[0]))
        else:
            return jsonify({"error": "No configuration data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Step 1: Parse config file
    config_data = parse_config("config.ini")

    # Step 2: Save to database
    if config_data:
        save_to_db(config_data)

    # Step 3: Run Flask API
    print("🚀 Starting Flask server at http://127.0.0.1:5000/get_config")
    app.run(debug=True)

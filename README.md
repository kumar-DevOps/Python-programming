# Configuration File Parser & API 🔧

## 📖 Overview
This project demonstrates how a **DevOps engineer** can automate configuration management tasks using Python.  
It reads a configuration file (`.ini` format), extracts key‑value pairs, saves them as JSON in a database, and exposes a REST API to fetch the stored configuration.

This ensures **consistency, automation, and easy access** to configuration data.

---

## 🛠 Features
- ✅ Reads `.ini` configuration files (e.g., `config.ini`)  
- ✅ Extracts key‑value pairs into a Python dictionary  
- ✅ Saves parsed data as JSON into a SQLite database  
- ✅ Provides a REST API (`GET /get_config`) using Flask  
- ✅ Handles errors gracefully (missing file, DB issues, etc.)  

---

## 📂 Project Structure
project/
│── config.ini                            # Sample configuration file
│── config_parser.py        # Main Python script
│── config_data.db          # SQLite database (auto-created)
│── README.md                              # Documentation

Code

---

## 📑 Sample Configuration File (`config.ini`)
```ini
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
⚙️ How It Works
Parse Config File → Reads config.ini using configparser.

Store in Database → Saves extracted data as JSON in SQLite.

Expose API → Flask provides a GET endpoint to fetch the latest configuration.

📦 Requirements
Python 3.x

Install dependencies:

bash
pip install flask
(configparser, json, and sqlite3 are built into Python.)

▶️ Usage
Place your configuration file as config.ini in the project folder.

Run the script:

bash
python config_parser.py
The script will:

Parse the configuration file

Save JSON data into config_data.db

Start a Flask server

Access the API in your browser or via curl:

bash
http://127.0.0.1:5000/get_config
📊 Example Output
Console
Code
✅ Configuration data saved to database successfully.
🚀 Starting Flask server at http://127.0.0.1:5000/get_config
API Response
json
{
  "Database": {
    "host": "localhost",
    "port": "3306",
    "username": "admin",
    "password": "secret"
  },
  "Server": {
    "address": "192.168.0.1",
    "port": "8080"
  }
}
🛡 Error Handling
File not found → Prints warning and skips parsing.

Empty config file → Raises error message.

Database issues → Displays error without crashing.

API errors → Returns JSON error response.

🚀 Extensions (Optional)
Add POST endpoint to update configuration dynamically.

Integrate with Ansible/Puppet/Chef for enterprise config management.

Add logging to track changes over time.

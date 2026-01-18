# Configuration File Parser & API 🔧

## 📖 Overview
This project demonstrates how a **DevOps engineer** can automate configuration management tasks using Python.  
It reads a configuration file (`.ini` format), extracts key‑value pairs, saves them as JSON in a SQLite database, and exposes a REST API to fetch the stored configuration.

This ensures **consistency, automation, and easy access** to configuration data.

---

## 🛠 Features
- ✅ Reads `.ini` configuration files (e.g., `config.ini`)  
- ✅ Extracts key‑value pairs into a Python dictionary  
- ✅ Saves parsed data as JSON into a SQLite database  
- ✅ Provides a REST API (`GET /get_config`) using Flask  
- ✅ Handles errors gracefully (missing file, DB issues, etc.)  

---

## 🔧 Prerequisites
- Python 3.8+ installed on your system  
- pip package manager  
- (Optional) Virtual environment for clean setup  

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

🚀 Setup Instructions
Clone the repository:

bash
git clone https://github.com/kumar-DevOps/Python-programming.git
cd Python-programming
git checkout Task3
Create a virtual environment (recommended):

bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies:

bash
pip install flask
Run the parser:

bash
python config_parser.py
Access the API:

Browser: http://127.0.0.1:5000/get_config

Curl:

bash
curl http://127.0.0.1:5000/get_config
Postman: Create a GET request to the same URL.

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
🗄 Database
The script creates a SQLite database file named config_data.db.

Each run inserts the latest configuration JSON.

You can inspect it using:

bash
sqlite3 config_data.db
.tables
SELECT * FROM config_data;
🛡 Error Handling
File not found → Prints warning and skips parsing.

Empty config file → Raises error message.

Database issues → Displays error without crashing.

API errors → Returns JSON error response.

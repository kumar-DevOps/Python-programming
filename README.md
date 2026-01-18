# Backup Script 🔐

## 📖 Overview
Regular backups are essential in DevOps to protect important files and ensure business continuity.  
This project provides a simple Python script (`backup.py`) that copies files from a **source directory** to a **destination directory**, ensuring unique filenames by appending timestamps when duplicates exist.

---

## 🛠 Features
- ✅ Copies all files from source → destination  
- ✅ Appends a timestamp if a file with the same name already exists in destination  
- ✅ Preserves file metadata (timestamps, permissions) using `shutil.copy2`  
- ✅ Handles errors gracefully (missing directories, permission issues, etc.)  
- ✅ Provides clear feedback for each file copied  

---

## 🔧 Prerequisites
- Python 3.8+ installed on your system  
- Basic knowledge of command-line usage  

---

## 📂 Project Structure
project/
│── backup.py                    # Main backup script
│── README.md                    # Documentation

Code

---

## ▶️ Usage
Run the script from the command line:

```bash
python backup.py <source_directory> <destination_directory>
Example
bash
python backup.py /home/user/documents /home/user/backups
📊 Example Output
Code
✅ Backed up: report.txt → /home/user/backups/report.txt
✅ Backed up: data.csv → /home/user/backups/data.csv
✅ Backed up: notes.txt → /home/user/backups/notes_20260118175930.txt
🎉 Backup completed successfully.
🛡 Error Handling
Source directory not found → Prints error and exits.

Destination directory not found → Prints error and exits.

Permission issues → Displays error message without crashing.

Unexpected errors → Caught and displayed gracefully.

⚙️ How It Works
The script checks if both source and destination directories exist.

Iterates through all files in the source directory.

If a file already exists in destination, appends a timestamp (YYYYMMDDHHMMSS) to ensure uniqueness.

Copies the file using shutil.copy2 to preserve metadata.

Prints a success message for each file copied.

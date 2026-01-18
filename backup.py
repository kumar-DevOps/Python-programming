import os
import sys
import shutil
import time

def backup_files(source_dir: str, dest_dir: str):
    """
    Backup files from source_dir to dest_dir.
    If a file already exists in dest_dir, append a timestamp to its name.
    """
    try:
        # Check if source exists
        if not os.path.exists(source_dir):
            print(f"❌ Error: Source directory '{source_dir}' does not exist.")
            return

        # Check if destination exists
        if not os.path.exists(dest_dir):
            print(f"❌ Error: Destination directory '{dest_dir}' does not exist.")
            return

        # Iterate through files in source directory
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Only copy files (skip directories)
            if os.path.isfile(source_path):
                # If file already exists in destination, append timestamp
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(filename)
                    timestamp = time.strftime("%Y%m%d%H%M%S")
                    new_filename = f"{base}_{timestamp}{ext}"
                    dest_path = os.path.join(dest_dir, new_filename)

                # Copy file
                shutil.copy2(source_path, dest_path)
                print(f"✅ Backed up: {filename} → {dest_path}")

        print("🎉 Backup completed successfully.")

    except Exception as e:
        print(f"⚠️ Error during backup: {e}")


if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)

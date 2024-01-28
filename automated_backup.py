import shutil
import subprocess
import datetime

SOURCE_DIR = "/path/to/source"
DESTINATION_DIR = "/path/to/destination"

def perform_backup():
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_folder = f"{DESTINATION_DIR}/backup_{timestamp}"

        shutil.copytree(SOURCE_DIR, backup_folder)

        print(f"Backup successful. Backup stored in {backup_folder}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

if __name__ == "__main__":
    success = perform_backup()

    if success:
        subprocess.run(["echo", "Backup Successful"])
    else:
        subprocess.run(["echo", "Backup Failed"])

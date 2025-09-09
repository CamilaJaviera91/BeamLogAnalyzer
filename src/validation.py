import os
import re

LOG_PATTERN = re.compile(r'(\S+ \S+) (\S+) (\S*) (\d{3}) (\d+)ms')

def validate_log_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            if not LOG_PATTERN.match(line.strip()):
                return False
    return True

def validate_logs_in_folder(folder="data/raw"):
    results = {}
    for filename in os.listdir(folder):
        if filename.endswith(".log"):
            filepath = os.path.join(folder, filename)
            is_valid = validate_log_file(filepath)
            results[filename] = "✅ OK" if is_valid else "❌ ERRORS"
    return results

if __name__ == "__main__":
    folder = "src/data/raw"
    results = validate_logs_in_folder(folder)
    for file, status in results.items():
        print(f"{file}: {status}")

import os
import re
import csv
import json

# Regular expression pattern to validate each log line.
# Expected format example:
# "2025-10-12 14:33:45 GET /api/users 200 123ms"
# Groups:
#   1. Timestamp (date and time)
#   2. HTTP method
#   3. Endpoint (optional)
#   4. HTTP status code (3 digits)
#   5. Response time (in milliseconds)
LOG_PATTERN = re.compile(r'(\S+ \S+) (\S+) (\S*) (\d{3}) (\d+)ms')

def validate_log_file(filepath):
    """
    Validate a single log file line by line.
    
    Args:
        filepath (str): Path to the log file to be validated.
    
    Returns:
        list[dict]: A list of dictionaries containing details about invalid lines.
    """
    errors = []
    with open(filepath, "r") as f:
        for i, line in enumerate(f, start=1):
            if not LOG_PATTERN.match(line.strip()):
                errors.append({
                    "file": os.path.basename(filepath),
                    "line_number": i,
                    "bad_line": line.strip()
                })
    return errors

def validate_logs_in_folder(folder="src/data/raw", report_folder="src/data/validation"):
    all_errors = []

    os.makedirs(report_folder, exist_ok=True)

    for filename in os.listdir(folder):
        if filename.endswith(".log"):
            filepath = os.path.join(folder, filename)
            errors = validate_log_file(filepath)
            all_errors.extend(errors)

            if not errors:
                print(f"✅ {filename}: All lines valid.")
            else:
                print(f"❌ {filename}: Found {len(errors)} invalid lines.")

    csv_path = os.path.join(report_folder, "log_validation_report.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["file", "line_number", "bad_line"])
        writer.writeheader()
        writer.writerows(all_errors)

    json_path = os.path.join(report_folder, "log_validation_report.json")
    with open(json_path, "w") as jsonfile:
        json.dump(all_errors, jsonfile, indent=4)

    print(f"\n📄 Report saved in:\n   - {csv_path}\n   - {json_path}")

if __name__ == "__main__":
    validate_logs_in_folder("src/data/raw", "src/data/validation")

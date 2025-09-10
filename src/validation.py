import os
import re

LOG_PATTERN = re.compile(r'(\S+ \S+) (\S+) (\S*) (\d{3}) (\d+)ms')

def validate_log_file(filepath):
    errors = []
    with open(filepath, "r") as f:
        for i, line in enumerate(f, start=1):
            if not LOG_PATTERN.match(line.strip()):
                errors.append((i, line.strip()))
    return errors

def validate_logs_in_folder(folder="data/raw"):
    for filename in os.listdir(folder):
        if filename.endswith(".log"):
            filepath = os.path.join(folder, filename)
            errors = validate_log_file(filepath)
            
            if not errors:
                print(f"✅ {filename}: All lines valid")
            else:
                print(f"❌ {filename}: Found {len(errors)} invalid lines")
                for line_num, bad_line in errors[:5]: 
                    print(f"   → Line {line_num}: {bad_line}")
                if len(errors) > 5:
                    print(f"   ... and {len(errors)-5} more errors")

if __name__ == "__main__":
    validate_logs_in_folder("data/raw")

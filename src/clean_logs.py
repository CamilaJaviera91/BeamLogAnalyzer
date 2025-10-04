import re
from datetime import datetime
import os

# Define input and output file paths
INPUT_FILE = "src/data/raw/logs.log"
OUTPUT_FILE = "src/data/clean/logs_clean.log"

LOG_PATTERN = re.compile(r'(\d{4}[-/]\d{2}[-/]\d{2}[ T-]\d{2}:\d{2}:\d{2}) (\w+) (\S+) (\d{3}) (\d+)ms')

def clean_logs(input_file, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(input_file, "r") as f, open(output_file, "w") as out:
        for line in f:
            match = LOG_PATTERN.match(line.strip())
            if not match:
                continue
            
            raw_time, method, endpoint, status, response_time = match.groups()

            try:
                if "/" in raw_time:
                    dt = datetime.strptime(raw_time, "%Y/%m/%d-%H:%M:%S")
                else:
                    dt = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S")
                timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue
            
            out.write(f"{timestamp} {method} {endpoint} {status} {response_time}ms\n")

if __name__ == "__main__":
    clean_logs(INPUT_FILE, OUTPUT_FILE)
    print(f"✅ Cleaned logs saved to {OUTPUT_FILE}")

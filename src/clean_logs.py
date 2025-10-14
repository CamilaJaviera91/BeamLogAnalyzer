import re
from datetime import datetime
import os
import logging

# Define input and output file paths
INPUT_FILE  = "src/data/raw/logs.log"
OUTPUT_FILE = "src/data/clean/logs_clean.log"
LOG_FILE    = "src/data/clean/clean_logs_report.log"

# Regular expression to match log lines with the following pattern:
#   1. Timestamp (supports YYYY-MM-DD HH:MM:SS or YYYY/MM/DD-HH:MM:SS)
#   2. HTTP method (e.g., GET, POST)
#   3. Endpoint (e.g., /api/users)
#   4. Status code (e.g., 200)
#   5. Response time in milliseconds (e.g., 123ms)
LOG_PATTERN = re.compile(r'(\d{4}[-/]\d{2}[-/]\d{2}[ T-]\d{2}:\d{2}:\d{2}) (\w+) (\S+) (\d{3}) (\d+)ms')

# Configure logger
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def clean_logs(input_file, output_file):
    """
    Cleans raw log data by:
      - Filtering only valid log lines matching the defined pattern.
      - Normalizing timestamps into a consistent format (YYYY-MM-DD HH:MM:SS).
      - Writing cleaned lines into a new output file.
      - Logging statistics of the cleaning process.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    total_lines = 0
    cleaned_lines = 0
    skipped_lines = 0
    timestamp_errors = 0
    
    # Open both input and output files
    with open(input_file, "r") as f, open(output_file, "w") as out:
        # Process each line in the input file
        for line in f:
            # Try to match the log line against the regex pattern
            match = LOG_PATTERN.match(line.strip())
            if not match:
                # Skip lines that don't follow the expected format
                continue
            
            # Extract the matched log components
            raw_time, method, endpoint, status, response_time = match.groups()

            try:
                # Normalize timestamp to a consistent format
                if "/" in raw_time:
                    # Handle format like 'YYYY/MM/DD-HH:MM:SS'
                    dt = datetime.strptime(raw_time, "%Y/%m/%d-%H:%M:%S")
                else:
                    # Handle format like 'YYYY-MM-DD HH:MM:SS'
                    dt = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S")
                timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                # Skip lines with invalid date formats
                continue
            
            # Write the cleaned and standardized log line to output file
            out.write(f"{timestamp} {method} {endpoint} {status} {response_time}ms\n")
        
    # Log final summary
    logging.info(f"Total lines processed: {total_lines}")
    logging.info(f"✅ Cleaned lines: {cleaned_lines}")
    logging.warning(f"⚠️ Skipped lines (invalid format): {skipped_lines}")
    logging.warning(f"🕒 Timestamp parsing errors: {timestamp_errors}")
    logging.info(f"Cleaned logs saved to {output_file}")

# Run the cleaning function if executed as a script
if __name__ == "__main__":
    clean_logs(INPUT_FILE, OUTPUT_FILE)
    print(f"✅ Cleaned logs saved to {OUTPUT_FILE}")

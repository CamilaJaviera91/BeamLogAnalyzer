import random
from datetime import datetime, timedelta
from faker import Faker
import os 

# Initialize the Faker library to generate fake data if needed
fake = Faker()

# Define output directory and file paths
OUTPUT_DIR = "src/data/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "logs.log")

# Possible API endpoints that simulate a web application's routes
ENDPOINTS = ["/api/users",
             "/api/orders",
             "/api/products",
             "/api/cart",
             "/api/payments",
             "/api/reviews"]

# Possible HTTP methods
METHODS = ["GET", "POST", "PUT", "DELETE"]

STATUS_CODES = [200, 201, 400, 401, 403, 404, 500, 502, 503]
STATUS_WEIGHTS = [0.6, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.025, 0.025]

def generate_log_line(base_time):
    """
    Generates a single simulated log line with possible data irregularities.
    """
    # Format timestamp as a readable string
    timestamp = base_time.strftime('%Y-%m-%d %H:%M:%S')
    # Randomly pick a method, endpoint, and weighted status code
    method = random.choice(METHODS)
    endpoint = random.choice(ENDPOINTS)
    status = random.choices(STATUS_CODES, weights=STATUS_WEIGHTS, k=1)[0]
    # Simulate a random response time in milliseconds
    response_time = random.randint(50, 500)

    # Introduce random noise or errors to simulate dirty data
    if random.random() < 0.05:
        endpoint = "" # Missing endpoint
    if random.random() < 0.05:
        status = 999 # Invalid status code
    if random.random() < 0.03:
        response_time = random.choice([-100, 99999]) # Out-of-range response times
    if random.random() < 0.02:
        timestamp = base_time.strftime("%Y/%m/%d-%H:%M:%S") # Non-standard timestamp format
    if random.random() < 0.01:
        return "BAD_LOG_LINE" # Corrupted line
    
    # Construct a valid log line
    return f"{timestamp} {method} {endpoint} {status} {response_time}ms"

def generate_logs(num_lines=500):
    """
    Generates multiple log lines and writes them to a file.
    """
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Base time used to increment timestamps
    base_time = datetime.now()

    with open(OUTPUT_FILE, "w") as f:
        for i in range(num_lines):
            log_time = base_time + timedelta(seconds=i * random.randint(1, 5))
            f.write(generate_log_line(log_time) + "\n")
    
    print(f"✅ Generate {num_lines} logs at {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_logs(2000)
    
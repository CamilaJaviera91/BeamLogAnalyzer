import random
from datetime import datetime, timedelta
from faker import Faker
import os 

fake = Faker()

OUTPUT_DIR = "data/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "logs.log")

ENDPOINTS = ["/api/users",
             "/api/orders",
             "/api/products",
             "/api/cart",
             "/api/payments",
             "/api/reviews"]

METHODS = ["GET", "POST", "PUT", "DELETE"]

STATUS_CODES = [200, 201, 400, 401, 403, 404, 500, 502, 503]
STATUS_WEIGHTS = [0.6, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.025, 0.025]
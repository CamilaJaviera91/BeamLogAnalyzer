# Beam Log Analyzer 
## Log Analyzer with Apache Beam

### 🛠️ Pipeline flow

- **Input:** simulated logs in a .log file (you can generate them with Faker or use an Apache/Nginx dataset).

- **Example lines:**

```
2025-09-06 12:34:56 GET /api/users 200 123ms
2025-09-06 12:35:02 GET /api/orders 500 234ms
2025-09-06 12:35:08 POST /api/cart 404 89ms
```

- **Format:**

```
TIMESTAMP METHOD ENDPOINT STATUS_CODE RESPONSE_TIME
```

- **Pipeline:**

    - Parse each line into a dictionary:
        - timestamp, method, endpoint, status_code, response_time
    
    - Classify status codes: 
        - 2xx = success 
        - 4xx = client error 
        - 5xx = server error
    
    - Count requests per minute.
    
    - Find the top 3 most requested endpoints.
    
    - Calculate the average response_time.

- **Output:**
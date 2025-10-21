# Beam Log Analyzer

## 📊 Log Analyzer with Apache Beam

This project demonstrates how to process and analyze **web server logs** using **Apache Beam**.  
It simulates log data, parses it, validates it, and generates meaningful insights such as request counts, response times, and top endpoints.

---

### 🚀 Features

- Simulates or ingests log lines in format.
- Log validation: detects malformed lines (missing fields, bad timestamps, etc).  
Parses valid lines into structured records: `timestamp`, `method`, `endpoint`, `status_code`, `response_time`.  
- Classifies status codes into categories: 2xx (success), 4xx (client error), 5xx (server error). 
- Computes metrics such as: 
    - Requests per minute  
    - Average response time  
    - Top N most requested endpoints  
    - Outputs reports in CSV and JSON formats:
        - `logs_summary.csv` → per-minute metrics.
        - `top_endpoints.csv` → ranking of endpoints.
        - `log_validation_report.csv` / `.json` → list of invalid log lines with details.

---

### 🧪 Tech Stack

- Python (>= 3.11).
- Apache Beam (batch mode).
- Faker (for synthetic log generation).  
- CSV / JSON for report output.

---

### 📁 Repository Structure

```
.
└── src
    ├── data
    │   ├── clean
    │   │   ├── clean_logs_report.log
    │   │   └── logs_clean.log
    │   ├── raw
    │   │   └── logs.log
    │   └── validation
    │       ├── log_validation_report.csv
    │       └── log_validation_report.json
    ├── clean_logs.py
    ├── generate_logs.py
    └── validation.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

### 🛠️ Pipeline flow

#### Input: 

- Logs are simulated in a `logs.log` file (generated with **Faker** or taken from an **Apache/Nginx dataset**).  
- ⚠️ The dataset is **not clean** and intentionally contains some **invalid or corrupted log lines**, such as:  
    - Missing fields (e.g., no endpoint or no response time).
    - Malformed timestamps.

This ensures the pipeline also handles **data quality validation**.

#### Example lines:

```
2025-09-07 22:08:59 DELETE /api/cart 200 241ms
2025-09-07 22:08:18 POST /api/payments 200 94ms
BAD_LOG_LINE
2025-09-07 22:08:44 POST /api/reviews 200 66ms
2025/09/07-22:10:23 PUT /api/orders 200 74ms
```

- **Format:**

```
TIMESTAMP METHOD ENDPOINT STATUS_CODE RESPONSE_TIME
```

- **Pipeline:**

    - Parse each line into a dictionary:
        - `timestamp`, `method`, `endpoint`, `status_code`, `response_time`
    
    - Classify status codes: 
        - `2xx` → success 
        - `4xx` → client error 
        - `5xx` → server error
    
    - Metrics & Analysis: 
        - Count **requests per minute**.
        - Find **Top 3 most requested endpoints**.
        - Calculate **average response_time**.

- **Output:**

    - `logs_summary.csv` → metrics per minute.
    - `top_endpoints.csv` → endpoint ranking.
    - `log_validation_report.csv` → list of invalid log lines with error details.
    - `log_validation_report.json` → list of invalid log lines with error details.

---

### 🧩 Usage & Customization

- You can customize the log pattern (in LOG_PATTERN) if your log format differs.
- Adjust the window or aggregation logic in Apache Beam if you want e.g., sliding windows, hourly metrics, etc.

---
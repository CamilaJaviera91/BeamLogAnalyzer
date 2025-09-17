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
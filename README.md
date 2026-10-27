# Sales Data ETL Pipeline Using Python and SQL

## 📌 Project Overview

The **Sales Data ETL Pipeline** is a beginner-friendly data engineering project that demonstrates how raw sales data can be transformed into clean, structured, and analysis-ready data.

The project follows the ETL (Extract, Transform, Load) process using Python, Pandas, and SQLite. It cleans raw sales records, handles missing and invalid values, removes duplicate records, calculates revenue, and loads the processed data into a SQLite database for SQL-based analysis.

## 🎯 Objectives

- Build an end-to-end ETL pipeline using Python.
- Clean and validate raw sales data.
- Remove duplicate records and handle missing or invalid values.
- Calculate revenue using quantity and unit price.
- Store cleaned data in a SQLite database.
- Analyze sales performance using SQL queries.
- Generate a data quality report and validate the pipeline with tests.

## 🛠️ Technologies Used

- **Python** — ETL pipeline implementation
- **Pandas** — Data cleaning and transformation
- **SQLite** — Data storage
- **SQL** — Sales analysis and aggregation
- **Pytest** — Automated testing
- **JSON** — Data quality reporting
- **Git and GitHub** — Version control and project hosting

## 🔄 ETL Workflow

1. **Extract:** Read raw sales data from a CSV file.
2. **Transform:** Clean the data, remove duplicates, handle missing or invalid records, and calculate revenue.
3. **Load:** Store the cleaned records in a SQLite database.
4. **Analyze:** Execute SQL queries to analyze sales and product performance.
5. **Validate:** Generate a data quality report and run automated tests.

## 📂 Project Structure

```text
sales-data-etl-pipeline/
│
├── data/
│   └── sales_raw.csv
│
├── tests/
│   └── test_pipeline.py
│
├── main.py
├── queries.sql
├── requirements.txt
├── README.md
└── .gitignore
```

Generated files, such as the SQLite database and data quality report, are created when the pipeline runs and are excluded from version control.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- A code editor such as Visual Studio Code

### 1. Clone the repository

```bash
git clone https://github.com/Manasagundavarapu/sales-data-etl-pipeline.git
cd sales-data-etl-pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If you use Command Prompt instead of PowerShell:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the ETL Pipeline

Execute the following command:

```bash
python main.py
```

The pipeline processes the raw CSV data, cleans the records, loads the results into SQLite, and generates a data quality report.

### Expected Output

```text
ETL pipeline completed successfully.
Raw rows: 16
Clean rows: 11
Rows removed: 5
SQLite database: sales.db
Quality report: data_quality_report.json
```

*Note: These results correspond to the sample dataset included in this project.*

## 📊 SQL Analysis

The project includes SQL queries in `queries.sql` to analyze the processed sales data.

### 1. Total Orders and Revenue

```sql
SELECT
    COUNT(*) AS order_count,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales;
```

**Sample result:**

| Metric | Value |
|---|---:|
| Cleaned records | 11 |
| Total revenue | 989.00 |

### 2. Product Performance

```sql
SELECT
    product,
    SUM(quantity) AS units_sold,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
```

This query identifies products with the highest revenue and summarizes the quantity sold.

### 3. Monthly Revenue Analysis

```sql
SELECT
    SUBSTR(order_date, 1, 7) AS month,
    ROUND(SUM(revenue), 2) AS monthly_revenue
FROM sales
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY month;
```

This query summarizes revenue by month to help identify sales trends.

## 🧪 Testing

Run the automated tests using:

```bash
python -m pytest -v
```

The tests validate the ETL pipeline's behavior and help identify issues during data processing.

## 📈 Key Features

- Automated CSV data ingestion
- Data cleaning and validation
- Duplicate record removal
- Missing and invalid data handling
- Revenue calculation
- SQLite database loading
- SQL-based sales analytics
- JSON data quality reporting
- Automated test coverage

## 🚀 Future Enhancements

- Schedule ETL runs automatically.
- Add logging and error-handling mechanisms.
- Connect to a cloud data warehouse such as Amazon Redshift.
- Orchestrate workflows using Apache Airflow.
- Add data visualizations and sales dashboards.
- Implement incremental data loading for larger datasets.

## 💡 Learning Outcomes

This project demonstrates practical understanding of ETL fundamentals, Python-based data transformation, relational databases, SQL aggregation, data quality checks, and automated testing.

## 👩‍💻 Author

**Manasa Gundavarapu**

GitHub: [Manasagundavarapu](https://github.com/Manasagundavarapu)

---

If you find this project useful, feel free to explore the repository and suggest improvements.

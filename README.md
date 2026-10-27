# Sales Data ETL Pipeline

A beginner-friendly data engineering project that extracts raw sales data from CSV, validates and transforms it with Python/Pandas, loads it into SQLite, and produces a data quality report.

## Architecture

`CSV source -> Extract -> Validate/Clean -> Calculate revenue -> SQLite -> SQL analysis`

## Tech stack

- Python 3.10+
- Pandas
- SQLite (included with Python)
- unittest (included with Python)
- Git and GitHub

## Features

- Reads raw sales records from CSV.
- Checks that required columns exist.
- Parses dates and numeric fields.
- Removes duplicate order IDs.
- Drops records with missing/unparseable critical fields.
- Rejects non-positive quantities and negative unit prices.
- Calculates order revenue.
- Loads clean records into a SQLite `sales` table.
- Writes row counts to `data_quality_report.json`.
- Includes SQL analytics queries and automated unit tests.

## Setup in VS Code

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependency

```bash
python -m pip install -r requirements.txt
```

### 3. Run the pipeline

```bash
python main.py
```

Expected summary: the pipeline completes, reports input and output row counts, and creates `sales.db` plus `data_quality_report.json`.

### 4. Run tests

```bash
python -m unittest discover -s tests -v
```

### 5. Run SQL queries

Open `sales.db` with a SQLite viewer extension in VS Code, or use Python's SQLite tools. The queries are in `queries.sql`.

## Data quality rules

- `order_id`, `order_date`, `customer_id`, `product`, `quantity`, and `unit_price` are required.
- The first row for a duplicate `order_id` is retained.
- Rows with missing required values or invalid dates are removed.
- Quantity must be a positive whole number.
- Unit price must be zero or greater.

For this demo, duplicate order IDs are assumed to represent duplicate orders. In a real system, confirm the business key and deduplication policy with stakeholders.

## Example SQL questions

1. What is total revenue?
2. Which products generate the most revenue?
3. How does revenue change by month?
4. Are there duplicate order IDs in the target table?

## Project structure

```text
sales-data-etl-pipeline/
├── data/
│   └── sales_raw.csv
├── tests/
│   └── test_pipeline.py
├── main.py
├── queries.sql
├── requirements.txt
├── README.md
└── .gitignore
```

## Possible next improvements

- Add logging and retry handling.
- Move configuration into environment variables or a config file.
- Add a timestamped run history and incremental loading.
- Schedule the pipeline with Airflow.
- Store data in PostgreSQL or a cloud data warehouse.
- Add a CI workflow that runs the tests on every GitHub push.

## Resume description

**Sales Data ETL Pipeline | Python, Pandas, SQL, SQLite**
- Built an ETL workflow to ingest sales data from CSV, validate records, remove duplicates, and calculate revenue.
- Loaded transformed data into SQLite and wrote SQL queries for product-level and monthly revenue analysis.
- Added automated unit tests and a data quality report to validate pipeline behavior.

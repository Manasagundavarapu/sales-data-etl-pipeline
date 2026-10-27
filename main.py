from pathlib import Path
import sqlite3
import json
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_FILE = DATA_DIR / "sales_raw.csv"
DB_FILE = BASE_DIR / "sales.db"
REPORT_FILE = BASE_DIR / "data_quality_report.json"

REQUIRED_COLUMNS = [
    "order_id", "order_date", "customer_id", "product",
    "quantity", "unit_price"
]


def extract(path: Path = RAW_FILE) -> pd.DataFrame:
    """Read raw sales records from CSV."""
    if not path.exists():
        raise FileNotFoundError(f"Input CSV not found: {path}")
    return pd.read_csv(path)


def transform(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Validate, clean, and enrich raw sales records."""
    missing_columns = sorted(set(REQUIRED_COLUMNS) - set(raw.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    input_rows = len(raw)
    df = raw[REQUIRED_COLUMNS].copy()

    # Normalize text fields and parse dates/numbers.
    for column in ["order_id", "customer_id", "product"]:
        df[column] = df[column].astype("string").str.strip()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # Remove duplicate order IDs, keeping the first occurrence.
    before_dedup = len(df)
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    duplicates_removed = before_dedup - len(df)

    # Drop rows with missing critical fields.
    before_missing = len(df)
    df = df.dropna(subset=REQUIRED_COLUMNS)
    missing_removed = before_missing - len(df)

    # Keep only plausible values.
    valid_mask = (
        (df["order_id"] != "") &
        (df["customer_id"] != "") &
        (df["product"] != "") &
        (df["quantity"] > 0) &
        (df["quantity"] % 1 == 0) &
        (df["unit_price"] >= 0)
    )
    before_invalid = len(df)
    df = df.loc[valid_mask].copy()
    invalid_removed = before_invalid - len(df)

    df["quantity"] = df["quantity"].astype(int)
    df["revenue"] = (df["quantity"] * df["unit_price"]).round(2)
    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

    report = {
        "input_rows": int(input_rows),
        "duplicates_removed": int(duplicates_removed),
        "rows_removed_for_missing_or_unparseable_values": int(missing_removed),
        "rows_removed_for_invalid_values": int(invalid_removed),
        "output_rows": int(len(df)),
        "rows_removed_total": int(input_rows - len(df)),
    }
    return df, report


def load_to_sqlite(clean: pd.DataFrame, db_path: Path = DB_FILE) -> None:
    """Replace the target table with the current clean dataset."""
    with sqlite3.connect(db_path) as connection:
        clean.to_sql("sales", connection, if_exists="replace", index=False)
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_sales_order_date ON sales(order_date)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_sales_product ON sales(product)"
        )


def run_pipeline() -> dict:
    """Run extract -> transform -> load and write a quality report."""
    raw = extract()
    clean, report = transform(raw)
    load_to_sqlite(clean)
    REPORT_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("ETL pipeline completed successfully.")
    print(f"Raw rows: {report['input_rows']}")
    print(f"Clean rows: {report['output_rows']}")
    print(f"Rows removed: {report['rows_removed_total']}")
    print(f"SQLite database: {DB_FILE.name}")
    print(f"Quality report: {REPORT_FILE.name}")
    return report


if __name__ == "__main__":
    run_pipeline()

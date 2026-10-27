import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent / "sales.db"

with sqlite3.connect(db_path) as conn:
    result = conn.execute("""
       SELECT order_id, COUNT(*) AS count
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1;
    """)

    print("Product | Units Sold | Revenue")
    for row in result.fetchall():
        print(row)
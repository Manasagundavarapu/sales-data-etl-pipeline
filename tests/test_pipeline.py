import unittest
import pandas as pd
from main import transform


class TestTransform(unittest.TestCase):
    def test_removes_duplicate_and_invalid_rows(self):
        raw = pd.DataFrame([
            {"order_id": "1", "order_date": "2026-01-01", "customer_id": "C1",
             "product": "Keyboard", "quantity": 2, "unit_price": 10},
            {"order_id": "1", "order_date": "2026-01-01", "customer_id": "C1",
             "product": "Keyboard", "quantity": 2, "unit_price": 10},
            {"order_id": "2", "order_date": "2026-01-02", "customer_id": "C2",
             "product": "Mouse", "quantity": 0, "unit_price": 5},
        ])
        clean, report = transform(raw)
        self.assertEqual(len(clean), 1)
        self.assertEqual(clean.iloc[0]["revenue"], 20)
        self.assertEqual(report["duplicates_removed"], 1)
        self.assertEqual(report["output_rows"], 1)

    def test_missing_column_raises_error(self):
        raw = pd.DataFrame([{"order_id": "1"}])
        with self.assertRaises(ValueError):
            transform(raw)


if __name__ == "__main__":
    unittest.main()

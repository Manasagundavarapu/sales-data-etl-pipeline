-- Run these queries after main.py has created sales.db.

-- 1. Total revenue and number of valid orders
SELECT COUNT(*) AS order_count, ROUND(SUM(revenue), 2) AS total_revenue
FROM sales;

-- 2. Revenue by product
SELECT product, SUM(quantity) AS units_sold, ROUND(SUM(revenue), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

-- 3. Monthly revenue
SELECT substr(order_date, 1, 7) AS month, ROUND(SUM(revenue), 2) AS revenue
FROM sales
GROUP BY month
ORDER BY month;

-- 4. Check for duplicate order IDs (should return no rows)
SELECT order_id, COUNT(*) AS count
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1;

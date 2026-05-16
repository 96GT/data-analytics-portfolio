
-- My first SQL practice query
-- Goal: Find total sales by product category

SELECT
  category,
  SUM(sales) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 04_purchase_trends.sql
-- Goal: review purchase and revenue trends over time.

SELECT
  PARSE_DATE('%Y%m%d', event_date) AS event_day,
  COUNTIF(event_name = 'purchase') AS purchase_events,
  COUNT(DISTINCT IF(event_name = 'purchase', user_pseudo_id, NULL)) AS purchasing_users,
  ROUND(SUM(COALESCE(ecommerce.purchase_revenue_in_usd, ecommerce.purchase_revenue, 0)), 2) AS revenue
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY event_day
ORDER BY event_day;

-- Weekly version for cleaner reporting.
SELECT
  DATE_TRUNC(PARSE_DATE('%Y%m%d', event_date), WEEK(MONDAY)) AS week_start,
  COUNTIF(event_name = 'purchase') AS purchase_events,
  COUNT(DISTINCT IF(event_name = 'purchase', user_pseudo_id, NULL)) AS purchasing_users,
  ROUND(SUM(COALESCE(ecommerce.purchase_revenue_in_usd, ecommerce.purchase_revenue, 0)), 2) AS revenue
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY week_start
ORDER BY week_start;

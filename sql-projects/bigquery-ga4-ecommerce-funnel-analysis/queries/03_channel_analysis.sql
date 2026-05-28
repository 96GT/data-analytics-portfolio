-- 03_channel_analysis.sql
-- Goal: compare traffic source / medium performance using available GA4 fields.
-- This does not calculate CAC or ROAS because ad spend is not available in this public dataset.

WITH user_source AS (
  SELECT
    user_pseudo_id,
    COALESCE(traffic_source.source, '(not set)') AS source,
    COALESCE(traffic_source.medium, '(not set)') AS medium,
    COUNT(*) AS event_count,
    COUNTIF(event_name = 'purchase') AS purchase_events,
    SUM(COALESCE(ecommerce.purchase_revenue_in_usd, ecommerce.purchase_revenue, 0)) AS revenue
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
  GROUP BY user_pseudo_id, source, medium
)
SELECT
  source,
  medium,
  COUNT(DISTINCT user_pseudo_id) AS users,
  SUM(event_count) AS events,
  SUM(purchase_events) AS purchase_events,
  ROUND(SAFE_DIVIDE(SUM(purchase_events), COUNT(DISTINCT user_pseudo_id)) * 100, 2) AS purchase_events_per_100_users,
  ROUND(SUM(revenue), 2) AS revenue
FROM user_source
GROUP BY source, medium
HAVING users >= 100
ORDER BY purchase_events DESC, users DESC;

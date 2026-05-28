-- 01_dataset_exploration.sql
-- Goal: understand the public GA4 ecommerce sample dataset before building metrics.
-- Dataset: bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*

-- Date range, event volume, and user count by day.
SELECT
  PARSE_DATE('%Y%m%d', event_date) AS event_day,
  COUNT(*) AS event_count,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY event_day
ORDER BY event_day;

-- Event name inventory.
SELECT
  event_name,
  COUNT(*) AS event_count,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY event_name
ORDER BY event_count DESC;

-- Traffic source overview.
SELECT
  COALESCE(traffic_source.source, '(not set)') AS source,
  COALESCE(traffic_source.medium, '(not set)') AS medium,
  COUNT(*) AS event_count,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY source, medium
ORDER BY users DESC;

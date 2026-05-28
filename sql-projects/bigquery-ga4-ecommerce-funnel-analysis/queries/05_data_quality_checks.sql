-- 05_data_quality_checks.sql
-- Goal: check data completeness and quality before presenting findings.

-- Missing user IDs and basic event completeness.
SELECT
  COUNT(*) AS total_events,
  COUNTIF(user_pseudo_id IS NULL) AS events_missing_user_id,
  COUNTIF(event_name IS NULL) AS events_missing_event_name,
  COUNTIF(event_date IS NULL) AS events_missing_event_date
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131';

-- Events by platform and device category where available.
SELECT
  COALESCE(platform, '(not set)') AS platform,
  COALESCE(device.category, '(not set)') AS device_category,
  COUNT(*) AS event_count,
  COUNT(DISTINCT user_pseudo_id) AS users
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
GROUP BY platform, device_category
ORDER BY event_count DESC;

-- Duplicate-looking event check using event timestamp, name, and user.
-- This is not a perfect duplicate test, but it can flag suspicious repeated rows.
WITH event_keys AS (
  SELECT
    user_pseudo_id,
    event_timestamp,
    event_name,
    COUNT(*) AS row_count
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
  GROUP BY user_pseudo_id, event_timestamp, event_name
)
SELECT
  COUNT(*) AS duplicate_key_groups,
  SUM(row_count) AS rows_in_duplicate_key_groups
FROM event_keys
WHERE row_count > 1;

-- Purchase events with no recorded revenue.
SELECT
  COUNT(*) AS purchase_events,
  COUNTIF(COALESCE(ecommerce.purchase_revenue_in_usd, ecommerce.purchase_revenue, 0) = 0) AS purchase_events_with_zero_revenue
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
  AND event_name = 'purchase';

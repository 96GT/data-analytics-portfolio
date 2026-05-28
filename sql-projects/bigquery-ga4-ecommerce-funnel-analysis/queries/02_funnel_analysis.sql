-- 02_funnel_analysis.sql
-- Goal: measure user movement through common ecommerce funnel events.
-- Note: event names should be confirmed with 01_dataset_exploration.sql before final interpretation.

WITH user_funnel AS (
  SELECT
    user_pseudo_id,
    MAX(IF(event_name = 'session_start', 1, 0)) AS reached_session_start,
    MAX(IF(event_name = 'view_item', 1, 0)) AS reached_view_item,
    MAX(IF(event_name = 'add_to_cart', 1, 0)) AS reached_add_to_cart,
    MAX(IF(event_name = 'begin_checkout', 1, 0)) AS reached_begin_checkout,
    MAX(IF(event_name = 'purchase', 1, 0)) AS reached_purchase
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20201101' AND '20210131'
  GROUP BY user_pseudo_id
),
funnel_counts AS (
  SELECT '1. Session start' AS funnel_step, COUNTIF(reached_session_start = 1) AS users FROM user_funnel
  UNION ALL
  SELECT '2. View item', COUNTIF(reached_view_item = 1) FROM user_funnel
  UNION ALL
  SELECT '3. Add to cart', COUNTIF(reached_add_to_cart = 1) FROM user_funnel
  UNION ALL
  SELECT '4. Begin checkout', COUNTIF(reached_begin_checkout = 1) FROM user_funnel
  UNION ALL
  SELECT '5. Purchase', COUNTIF(reached_purchase = 1) FROM user_funnel
)
SELECT
  funnel_step,
  users,
  ROUND(users / FIRST_VALUE(users) OVER (ORDER BY funnel_step) * 100, 2) AS pct_of_first_step,
  ROUND(users / LAG(users) OVER (ORDER BY funnel_step) * 100, 2) AS pct_of_previous_step
FROM funnel_counts
ORDER BY funnel_step;

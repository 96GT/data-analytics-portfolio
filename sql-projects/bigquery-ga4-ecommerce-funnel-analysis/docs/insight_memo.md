# Insight Memo: BigQuery GA4 Ecommerce Funnel Analysis

## Status

In progress. The first dataset exploration outputs have been reviewed and summarized.

## Business Question

How can an ecommerce business understand funnel performance, traffic quality, and purchase behavior using event-level GA4 data?

## Data Used

- Public BigQuery dataset: `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
- Date range analyzed: `2020-11-01` to `2021-01-31`
- Dataset type: obfuscated ecommerce event data
- Outputs reviewed so far:
  - Daily event volume, daily users, and events per user
  - Event name inventory

## Method

1. Queried daily event volume and unique user counts from the GA4 ecommerce sample dataset.
2. Exported the summarized result to Google Sheets for review.
3. Calculated events per user as `event_count / users`.
4. Identified total event volume, average daily events, average daily users, peak activity day, and lowest activity day.
5. Queried the event name inventory to understand which user actions are tracked.
6. Reviewed the available event types before deeper funnel and channel analysis.

## Key Findings

### Finding 1: Event activity was highest in early December and declined around the holidays.

The dataset covers 92 days from 2020-11-01 to 2021-01-31, with 4,295,584 total events. Daily activity peaked on 2020-12-08 with 92,199 events and 6,689 users, while the lowest activity occurred on 2020-12-25 with 21,355 events and 2,491 users.

The overall event-to-daily-user ratio was 13.46 events per user. This suggests users generated about 13 to 14 tracked events per active day on average during the analysis period.

Daily activity appears strongest in early December and weaker during the late-December holiday period. This matters because funnel and purchase trends should be interpreted in the context of seasonal traffic changes rather than treated as evenly distributed activity.

### Finding 2: The dataset contains the key ecommerce events needed for funnel analysis.

The event inventory shows 17 tracked event types, including core ecommerce funnel steps such as `session_start`, `view_item`, `add_to_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, and `purchase`.

High-volume browsing events dominate total activity: `page_view` has 1,350,428 events, `user_engagement` has 1,058,721 events, and `scroll` has 493,072 events. Lower-funnel actions are much smaller: `add_to_cart` has 58,543 events, `begin_checkout` has 38,757 events, and `purchase` has 5,692 events.

Plain-English interpretation: many users browse, some users look at products, fewer users add products to cart, fewer users start checkout, and even fewer users purchase. This is the basic ecommerce funnel pattern.

This confirms the dataset can support funnel analysis, while also showing that purchase behavior represents a much smaller share of total activity than browsing and engagement events.

### Finding 3

To be completed after reviewing funnel, channel, or purchase trend outputs.

## Recommendation

Do not make funnel or channel recommendations from the exploration outputs alone. Use these first outputs as a data coverage and funnel-readiness check, then continue with funnel analysis, traffic source analysis, purchase trend analysis, and data quality checks before making business recommendations.

## Limitations

- This is public, obfuscated sample data and does not represent a private company.
- The first findings are based on daily event counts and event inventory, not user-level funnel conversion or channel performance.
- Event counts alone do not prove where users drop off; a user-level funnel query is needed for that.
- CAC, ROAS, and paid media efficiency cannot be calculated without campaign spend data.
- Subscription conversion cannot be calculated without subscription lifecycle data.
- Attribution analysis is limited without a defined attribution model and richer campaign touchpoint history.

## Next Steps

- Export the event name inventory result as `event_name_inventory.csv` if not already saved.
- Run the funnel analysis query and export the summarized result.
- Run traffic source and purchase trend queries.
- Add the final CSV outputs to the project when ready.
- Create a KPI summary and funnel chart after the core outputs are reviewed.
- Convert final findings into resume bullets after the project has enough completed analysis.

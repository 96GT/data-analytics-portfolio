# Insight Memo: BigQuery GA4 Ecommerce Funnel Analysis

## Status

In progress. `01_dataset_exploration.sql` has been reviewed and summarized.

## Business Question

How can an ecommerce business understand funnel performance, traffic quality, and purchase behavior using event-level GA4 data?

## Data Used

- Public BigQuery dataset: `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
- Date range analyzed: `2020-11-01` to `2021-01-31`
- Dataset type: obfuscated ecommerce event data
- Outputs reviewed so far:
  - Daily event volume, daily users, and events per user
  - Event name inventory
  - Traffic source overview

## Method

1. Used `01_dataset_exploration.sql` to understand the dataset before making performance claims.
2. Queried daily event volume and unique user counts from the GA4 ecommerce sample dataset.
3. Exported the summarized result to Google Sheets for review.
4. Calculated events per user as `event_count / users`.
5. Identified total event volume, average daily events, average daily users, peak activity day, and lowest activity day.
6. Queried the event name inventory to understand which user actions are tracked.
7. Reviewed the traffic source overview to understand where user volume appears to come from, while reserving performance conclusions for the dedicated channel analysis query.

## Query-To-Memo Map

- `01_dataset_exploration.sql`: supports early exploration, including data coverage, event inventory, and basic traffic source context.
- `02_funnel_analysis.sql`: will support the user-level funnel drop-off finding.
- `03_channel_analysis.sql`: will support source/medium performance analysis using purchase behavior and revenue where available.
- `04_purchase_trends.sql`: will support purchase and revenue trend findings.
- `05_data_quality_checks.sql`: will support data quality notes and limitations.

## Key Findings

### Query 1: Dataset Exploration

`01_dataset_exploration.sql` was used to understand the dataset before making funnel, channel, or performance recommendations. This query contains three exploration outputs: daily activity summary, event name inventory, and traffic source overview.

#### Query 1A: Daily Activity Summary

The dataset covers 92 days from 2020-11-01 to 2021-01-31, with 4,295,584 total events. Daily activity peaked on 2020-12-08 with 92,199 events and 6,689 users, while the lowest activity occurred on 2020-12-25 with 21,355 events and 2,491 users.

The overall event-to-daily-user ratio was 13.46 events per user. This suggests users generated about 13 to 14 tracked events per active day on average during the analysis period.

Daily activity appears strongest in early December and weaker during the late-December holiday period. This matters because funnel and purchase trends should be interpreted in the context of seasonal traffic changes rather than treated as evenly distributed activity.

Plain-English interpretation: the dataset has enough daily activity to analyze, but traffic is not flat across the whole period. Early December was much busier than Christmas and the surrounding holiday period.

#### Query 1B: Event Name Inventory

The event inventory shows 17 tracked event types, including core ecommerce funnel steps such as `session_start`, `view_item`, `add_to_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, and `purchase`.

High-volume browsing events dominate total activity: `page_view` has 1,350,428 events, `user_engagement` has 1,058,721 events, and `scroll` has 493,072 events. Lower-funnel actions are much smaller: `add_to_cart` has 58,543 events, `begin_checkout` has 38,757 events, and `purchase` has 5,692 events.

Plain-English interpretation: many users browse, some users look at products, fewer users add products to cart, fewer users start checkout, and even fewer users purchase. This is the basic ecommerce funnel pattern.

This confirms the dataset can support funnel analysis, while also showing that purchase behavior represents a much smaller share of total activity than browsing and engagement events.

#### Query 1C: Traffic Source Overview

The traffic source overview shows that `google / organic` and `(direct) / (none)` account for the largest user and event volume in the exploration output. `google / organic` produced 1,323,449 events and 103,487 users, while `(direct) / (none)` produced 989,684 events and 75,951 users.

Referral and other sources also contribute meaningful volume, including `<Other> / referral` with 412,242 events and 32,880 users, and `shop.googlemerchandisestore.com / referral` with 365,774 events and 26,065 users.

`google / cpc` appears in the dataset with 176,963 events and 15,527 users, but this output only shows traffic volume. It does not show purchases, revenue, ad spend, CAC, or ROAS.

Plain-English interpretation: this table tells where users came from, not whether those users were valuable. To evaluate channel performance, the analysis needs purchase behavior and revenue, which are handled later in `03_channel_analysis.sql`.

### Query 2: Funnel Analysis

To be completed after reviewing the user-level funnel analysis output from `02_funnel_analysis.sql`.

### Query 3: Channel Analysis

To be completed after reviewing source/medium performance from `03_channel_analysis.sql`.

### Query 4: Purchase Trends

To be completed after reviewing purchase and revenue trend outputs from `04_purchase_trends.sql`.

### Query 5: Data Quality Checks

To be completed after reviewing data quality outputs from `05_data_quality_checks.sql`.

## Recommendation

Do not make funnel or channel recommendations from the exploration outputs alone. Use `01_dataset_exploration.sql` as a data coverage, funnel-readiness, and traffic-composition check. Continue with funnel analysis, channel analysis, purchase trend analysis, and data quality checks before making business recommendations.

## Limitations

- This is public, obfuscated sample data and does not represent a private company.
- The first findings are based on daily event counts, event inventory, and traffic source volume, not user-level funnel conversion or channel performance.
- Event counts alone do not prove where users drop off; a user-level funnel query is needed for that.
- Traffic source volume alone does not prove source or channel quality; purchase behavior and revenue are needed for performance analysis.
- CAC, ROAS, and paid media efficiency cannot be calculated without campaign spend data.
- Subscription conversion cannot be calculated without subscription lifecycle data.
- Attribution analysis is limited without a defined attribution model and richer campaign touchpoint history.

## Next Steps

- Save the first query outputs as CSV files if not already saved:
  - `dataset_daily_summary.csv`
  - `event_name_inventory.csv`
  - `traffic_source_overview.csv`
- Run the funnel analysis query and export the summarized result.
- Run the dedicated channel analysis query and compare source/medium purchase behavior.
- Run purchase trend queries.
- Add the final CSV outputs to the project when ready.
- Create a KPI summary and funnel chart after the core outputs are reviewed.
- Convert final findings into resume bullets after the project has enough completed analysis.

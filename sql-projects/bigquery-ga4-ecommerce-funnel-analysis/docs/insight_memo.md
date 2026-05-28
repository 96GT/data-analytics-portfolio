# Insight Memo: BigQuery GA4 Ecommerce Funnel Analysis

## Status

In progress. The first dataset exploration output has been reviewed and summarized.

## Business Question

How can an ecommerce business understand funnel performance, traffic quality, and purchase behavior using event-level GA4 data?

## Data Used

- Public BigQuery dataset: `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
- Date range analyzed: `2020-11-01` to `2021-01-31`
- Dataset type: obfuscated ecommerce event data
- First output reviewed: daily event volume, daily users, and events per user

## Method

1. Queried daily event volume and unique user counts from the GA4 ecommerce sample dataset.
2. Exported the summarized result to Google Sheets for review.
3. Calculated events per user as `event_count / users`.
4. Identified total event volume, average daily events, average daily users, peak activity day, and lowest activity day.
5. Reviewed the output for broad activity patterns before deeper funnel and channel analysis.

## Key Findings

### Finding 1: Event activity was highest in early December and declined around the holidays.

The dataset covers 92 days from 2020-11-01 to 2021-01-31, with 4,295,584 total events. Daily activity peaked on 2020-12-08 with 92,199 events and 6,689 users, while the lowest activity occurred on 2020-12-25 with 21,355 events and 2,491 users.

The overall event-to-daily-user ratio was 13.46 events per user. This suggests users generated about 13 to 14 tracked events per active day on average during the analysis period.

Daily activity appears strongest in early December and weaker during the late-December holiday period. This matters because funnel and purchase trends should be interpreted in the context of seasonal traffic changes rather than treated as evenly distributed activity.

### Finding 2

To be completed after reviewing the event name inventory output.

### Finding 3

To be completed after reviewing funnel, channel, or purchase trend outputs.

## Recommendation

Do not make funnel or channel recommendations from the daily summary alone. Use this first output as a data coverage and activity check, then continue with event inventory, funnel analysis, traffic source analysis, purchase trend analysis, and data quality checks before making business recommendations.

## Limitations

- This is public, obfuscated sample data and does not represent a private company.
- This first finding is based on daily event and user counts only, not purchase behavior or channel performance.
- CAC, ROAS, and paid media efficiency cannot be calculated without campaign spend data.
- Subscription conversion cannot be calculated without subscription lifecycle data.
- Attribution analysis is limited without a defined attribution model and richer campaign touchpoint history.

## Next Steps

- Export the event name inventory result as `event_name_inventory.csv`.
- Confirm which GA4 ecommerce events are available for funnel analysis.
- Run the funnel analysis query and export the summarized result.
- Run traffic source and purchase trend queries.
- Add the final CSV outputs to the project when ready.
- Create a KPI summary and funnel chart after the core outputs are reviewed.
- Convert final findings into resume bullets after the project has enough completed analysis.

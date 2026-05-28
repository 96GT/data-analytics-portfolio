# Insight Memo: BigQuery GA4 Ecommerce Funnel Analysis

## Status

Draft template. Replace placeholders after running the SQL queries.

## Business Question

How can an ecommerce business understand funnel performance, traffic quality, and purchase behavior using event-level GA4 data?

## Data Used

- Public BigQuery dataset: `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
- Date range analyzed: `2020-11-01` to `2021-01-31`
- Dataset type: obfuscated ecommerce event data

## Method

1. Explored event names, user volume, traffic sources, and date coverage.
2. Built a user-level funnel across key ecommerce events.
3. Compared purchase behavior by traffic source and medium where available.
4. Reviewed purchase and revenue trends over time.
5. Ran data quality checks before interpreting results.

## Key Findings

Replace with findings after running the queries.

- Finding 1:
- Finding 2:
- Finding 3:

## Recommendation

Replace with recommendation after reviewing the results.

- Recommendation:

## Limitations

- This is public, obfuscated sample data and does not represent a private company.
- CAC, ROAS, and paid media efficiency cannot be calculated without campaign spend data.
- Subscription conversion cannot be calculated without subscription lifecycle data.
- Attribution analysis is limited without a defined attribution model and richer campaign touchpoint data.

## Next Steps

- Export query outputs for dashboarding.
- Create a KPI summary and funnel chart.
- Add a short deck or dashboard screenshot to the project.
- Convert the final project into resume bullets.

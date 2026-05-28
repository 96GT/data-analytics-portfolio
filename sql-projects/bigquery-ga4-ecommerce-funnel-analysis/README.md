# BigQuery GA4 Ecommerce Funnel Analysis

## Project Status

In progress.

## Project Goal

This project uses the public Google Analytics 4 ecommerce sample dataset in BigQuery to practice marketing analytics, funnel reporting, SQL querying, KPI reporting, and business insight writing.

The project is inspired by entry-level marketing analyst roles that ask for funnel analysis, dashboarding, campaign reporting, SQL, Excel/Sheets, and clear written recommendations.

## Dataset

Dataset: `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`

Source: Google Analytics 4 ecommerce sample export from the Google Merchandise Store.

This is not Rugiet data and does not represent any private company performance. The dataset is public and obfuscated.

## Business Questions

1. How many users move through key ecommerce funnel steps?
2. Where does the funnel show the largest drop-off?
3. Which traffic sources or mediums are associated with stronger purchase behavior?
4. How do purchases and revenue trend over time?
5. What data quality checks are needed before trusting the results?
6. Which marketing metrics cannot be calculated from this dataset without additional data?

## Metrics In Scope

- Users
- Sessions where available
- Event counts
- Funnel step users
- Purchase users
- Purchase events
- Revenue where available
- Conversion rates based on available event behavior
- Traffic source and medium performance

## Metrics Not Available Without Additional Data

The dataset may not support every metric in a real D2C marketing analyst role. These should not be invented.

- CAC requires marketing spend by channel or campaign.
- ROAS requires reliable ad spend and revenue by campaign.
- Paid media efficiency requires ad platform cost data.
- Subscription conversion requires subscription lifecycle data.
- Full attribution logic requires a defined attribution model and campaign touchpoint history.

## Repository Structure

```text
queries/
  01_dataset_exploration.sql
  02_funnel_analysis.sql
  03_channel_analysis.sql
  04_purchase_trends.sql
  05_data_quality_checks.sql
docs/
  insight_memo.md
```

## Planned Artifacts

- SQL queries written for BigQuery
- KPI summary tables exported from query results
- Dashboard or chart screenshots
- One-page insight memo
- Optional short presentation deck

## Skills Demonstrated

- BigQuery SQL
- Event-level ecommerce analysis
- Funnel reporting
- KPI definition
- Dashboard planning
- Data quality checks
- Business writing
- Clear communication of limitations

## Current Next Steps

1. Run `01_dataset_exploration.sql` in BigQuery.
2. Confirm available event names, date range, and revenue fields.
3. Run funnel analysis and identify the largest drop-off.
4. Analyze traffic source or medium performance.
5. Write a concise insight memo with findings and limitations.

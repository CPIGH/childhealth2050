# Indicator Explorer  ·  `/data`

**Tool 2 of 4.** The public data section of the site — browse and compare **indicators** across
countries and over time.

> This folder is a **subsite** (a page users visit at childhealth2050.org/data), *not* storage.
> The cleaned data files this page loads live in [assets/data/](../assets/data/); the code that
> builds them lives in [data-processing/](../data-processing/). See
> [docs/DECISIONS.md](../docs/DECISIONS.md).

## What it shows

- **Historical trends** for an indicator, with **indicator switching** and country selection.
- Comparison of multiple countries / a country vs. a regional average.
- A path toward the **Cause Explorer** view (cause-specific burden) as a future enhancement.

## Indicators (initial)

Mortality (U5MR, NMR), nutrition (stunting, wasting), coverage (DTP3, MCV1), burden (causes of
death, causes of DALYs), equity (wealth, sex, urban/rural). Full list in [PLAN.md](../PLAN.md).

## Content & data

- Indicator descriptions / methodology: [content/indicators/](../content/indicators/).
- Numbers: fetched on demand from [assets/data/](../assets/data/).

## Link sharing

State lives in the query string, for example `/data/?indicator=u5mr&countries=NGA,GHA&from=1990`.

## Status

A placeholder index.html exists, but the intended experience is a dashboard-first view with a
searchable country selector and simple defaults that make it easy to compare indicators quickly.

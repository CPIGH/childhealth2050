# Countries Like Mine  ·  `/countries-like-mine`

**Tool 3 of 4.** The heart of the platform's value proposition:

> *"What can I learn from countries like mine that achieved better child health outcomes?"*

## What it does

- **Comparator engine:** given a country, find the countries most similar to it along a set of
  dimensions — initial ones from the concept note: **baseline indicator, income, poverty,
  governance, health expenditure**. Returns a shortlist (e.g. top 5 comparators).
- **Positive deviants:** among those similar countries, highlight the ones that **did better**,
  and rank them (performance categories: *better / similar / worse*).
- **Compare workspace:** put a country side by side with a few comparators, or against a regional
  average.

Success test from the concept note: *a user can select Nigeria and identify comparable countries.*

## How it works (static site)

There's no live backend (see [ADR-002](../docs/DECISIONS.md)). The comparator either:

- runs **client-side** over a small precomputed similarity/features file, or
- reads **precomputed comparator lists** produced by [`data-processing/`](../data-processing/).

Pick whichever keeps the shipped data small and the interaction responsive.

## Content & data

- Method write-up / caveats: [`content/`](../content/) (indicator or a dedicated methods file).
- Comparator outputs the page reads: [`assets/data/`](../assets/data/).

## Link sharing

State in the query string, e.g. `/countries-like-mine/?country=NGA&by=income,mortality`.

## Status

A placeholder `index.html` exists (shared nav + description). No comparator built yet.

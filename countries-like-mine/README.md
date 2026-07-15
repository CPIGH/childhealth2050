# Countries Like Mine  ·  `/countries-like-mine`

**Tool 3 of 4.** The heart of the platform's value proposition:

> *"What can I learn from countries like mine that achieved better child health outcomes?"*

## What it does

- **Comparator engine:** given a country, find the countries most similar to it along a set of
  dimensions such as mortality, income, life expectancy, region, and other contextual characteristics.
- **Default-first experience:** the tool presents a sensible default shortlist automatically —
  the **3 closest** countries by the automated composite — so the user does not have to configure
  every choice up front.
- **Optional customization:** if the user wants, they can change the **number** of comparators
  (default 3), the weighting logic, or pick the exact **dimensions** to match on (e.g. "just GDP and
  mortality"), through a compact settings panel / pop-up. The automated basis is always listed clearly
  so users know what "similar" means.
- **Positive deviants:** among those similar countries, highlight the ones that **did better** and
  rank them (for example, *better / similar / worse*).

## How it works (static site)

There is no live backend (see [ADR-002](../docs/DECISIONS.md)). The comparator should use a small
precomputed similarity feature set and default comparator lists produced by [data-processing/](../data-processing/)
so the experience stays lightweight and responsive.

## Content & data

- Method write-up / caveats: [content/](../content/) (indicator or a dedicated methods file).
- Comparator outputs the page reads: [assets/data/](../assets/data/).

## Link sharing

State lives in the query string, for example `/countries-like-mine/?country=NGA&mode=auto`.

## Status

The page is still a placeholder, but the intended experience is a low-friction comparator flow with
an automated default path and a simple customization layer for more advanced users.

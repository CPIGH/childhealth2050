# Future Trajectories  ·  `/trajectories`

**Tool 4 of 4.** Where a country is heading — the **2050 outlook**.

## What it shows

- **Baseline forecasts** for the key indicators out toward 2050.
- **Forecast uncertainty** (intervals, not just a line).
- **Historical comparison** — the forecast in the context of the observed past trend.

## How it works (static site)

Forecasts are **precomputed** in [data-processing/](../data-processing/) and shipped as lean data files;
the page just renders them. No live modeling in the browser or on a server (see [ADR-002](../docs/DECISIONS.md)).

## Content & data

- Method notes / assumptions / caveats: [content/](../content/).
- Forecast series + intervals: [assets/data/](../assets/data/), fetched on demand.

## Link sharing

State lives in the query string, for example `/trajectories/?country=NGA&indicator=u5mr`.

## Status

A placeholder index.html exists, but the intended experience is a forecast view that remains easy to
access from country profiles and the broader dashboard flow.

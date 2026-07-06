# GeoRisk Simulator

A console-based geopolitical strategy simulator (work in progress).

This is the initial version of the project. There is no gameplay yet —
it only shows a title screen, lets you pick a country, and displays
that country's starting statistics.

## Files

- `main.py` — entry point; runs the title screen and country selection flow.
- `countries.py` — holds the country data (economy, military, stability, technology, population).
- `README.md` — this file.

## Countries

- United States
- China
- India
- Germany
- Brazil
- Japan

Each country has the following stats:

- **Economy**
- **Military**
- **Stability**
- **Technology**
- **Population**

## Running

```bash
python main.py
```

## Status

Gameplay mechanics (turns, events, interactions between countries, etc.)
are not implemented yet. This version only covers the title screen and
country selection/display.

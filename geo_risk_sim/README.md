# GeoRisk Simulator

A turn-based, console-only geopolitical strategy simulator written in
Python. Pick a nation, grow its economy, military, stability, and
technology, weather random world events, and see how you stack up
against five other world powers over a 20-year campaign.

## Features

- **Six playable countries** — United States, China, India, Germany,
  Brazil, and Japan — each with distinct starting stats.
- **Turn-based progression** from the year 2025 to 2045 (20 turns).
- **Four upgradeable stats** — Economy, Military, Stability, and
  Technology — each improvable by +5 per turn, capped at 100.
- **22 random geopolitical events** (booms, recessions, coups, cyber
  attacks, pandemics, and more) that fire when you advance the year,
  each nudging one or more stats up or down.
- **Power Score** — a country's overall strength: economy + military +
  stability + technology.
- **World Rankings** — every country ranked by Power Score, with your
  own rank highlighted.
- **Risk Score** — a measure of a country's instability, shown on the
  country report: `100 - Stability - Economy/2 - Military/4`.
- **Full input validation** — the game never crashes on bad input,
  and exits cleanly on Ctrl+C or Ctrl+D.

## Installation

Requires Python 3.6 or later (uses f-strings) and no external
dependencies.

```bash
git clone <repository-url>
cd geo_risk_sim
```

## How to Play

Run the game from the `geo_risk_sim` directory:

```bash
python3 main.py
```

1. Choose one of the six countries by entering its number.
2. Use the main menu each turn to:
   - **View Country** — see your current stats and Risk Score.
   - **Improve Economy / Build Military / Increase Stability /
     Research Technology** — spend a turn boosting one stat by 5.
   - **Advance Year** — move to the next year and trigger a random
     world event.
   - **World Rankings** — see how every country ranks by Power Score.
   - **Quit** — exit the game at any time.
3. The simulation automatically ends after reaching the year 2045.

## Python Concepts Demonstrated

- **Modular design** — the project is split across `main.py`
  (entry point and UI/game loop), `countries.py` (country data and
  stat mutation), `events.py` (event data and selection), and
  `calculations.py` (derived stats: Power Score and Risk Score).
- **Dictionaries** — nested dictionaries model country and event
  data; dict comprehensions build the Power Score rankings.
- **Functions** — each screen and game action is its own function
  with a single responsibility and a docstring.
- **Loops** — a `while` loop drives the main game loop and input
  re-prompting; `for` loops render menus and rankings.
- **Conditionals** — `if`/`elif` chains dispatch menu choices to the
  right handler.
- **The `random` module** — `random.choice()` selects each year's
  event.
- **String formatting** — f-strings with alignment specifiers
  (`:>3`, `:<15`) produce a clean, tabular console layout.
- **Error handling** — a `try`/`except` around the game loop catches
  `EOFError` and `KeyboardInterrupt` for a graceful exit.

## Future Improvements

- Persist game state to a file so a session can be saved and resumed.
- Add diplomacy or trade actions between countries.
- Let random events target other countries, not just the player's.
- Add a difficulty setting that scales event severity.
- Add unit tests for `countries.py`, `events.py`, and `calculations.py`.
- Add colored terminal output for stat increases/decreases.

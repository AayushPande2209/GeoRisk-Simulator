"""Country data for the GeoRisk Simulator.

This module holds the static starting data for each playable country.
"""

COUNTRIES = {
    "United States": {
        "economy": 90,
        "military": 95,
        "stability": 80,
        "technology": 95,
        "population": 331,
    },
    "China": {
        "economy": 85,
        "military": 90,
        "stability": 70,
        "technology": 85,
        "population": 1412,
    },
    "India": {
        "economy": 65,
        "military": 70,
        "stability": 60,
        "technology": 65,
        "population": 1408,
    },
    "Germany": {
        "economy": 80,
        "military": 55,
        "stability": 90,
        "technology": 90,
        "population": 84,
    },
    "Brazil": {
        "economy": 55,
        "military": 50,
        "stability": 55,
        "technology": 50,
        "population": 215,
    },
    "Japan": {
        "economy": 75,
        "military": 60,
        "stability": 85,
        "technology": 92,
        "population": 125,
    },
}


def get_country_names():
    return list(COUNTRIES.keys())


def get_country_stats(name):
    return COUNTRIES[name]


def increase_stat(name, stat, amount=5):
    stats = COUNTRIES[name]
    stats[stat] = min(100, stats[stat] + amount)


def apply_stat_delta(name, stat, delta):
    stats = COUNTRIES[name]
    before = stats[stat]

    if stat == "population":
        after = max(0, before + delta)
    else:
        after = max(0, min(100, before + delta))

    stats[stat] = after
    return after - before

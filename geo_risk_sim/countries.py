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
    """Return a list of all available country names."""
    return list(COUNTRIES.keys())


def get_country_stats(name):
    """Return the statistics dictionary for the given country name."""
    return COUNTRIES[name]

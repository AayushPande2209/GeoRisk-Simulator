"""Country power calculations for the GeoRisk Simulator."""

from countries import get_country_names, get_country_stats


def calculate_power(name):
    stats = get_country_stats(name)
    return stats["economy"] + stats["military"] + stats["stability"] + stats["technology"]


def get_power_rankings():
    powers = {name: calculate_power(name) for name in get_country_names()}
    return sorted(powers.items(), key=lambda item: item[1], reverse=True)


def calculate_risk(name):
    """Risk = 100 - Stability - Economy/2 - Military/4, clamped to 0-100."""
    stats = get_country_stats(name)
    raw_risk = 100 - stats["stability"] - stats["economy"] / 2 - stats["military"] / 4
    return max(0, min(100, round(raw_risk)))

"""Country power calculations for the GeoRisk Simulator."""

from countries import get_country_names, get_country_stats


def calculate_power(name):
    """Power Score = economy + military + stability + technology."""
    stats = get_country_stats(name)
    economy = stats["economy"]
    military = stats["military"]
    stability = stats["stability"]
    technology = stats["technology"]
    return economy + military + stability + technology


def get_power_rankings():
    """Return (name, power) tuples sorted strongest to weakest."""
    powers = {name: calculate_power(name) for name in get_country_names()}
    return sorted(powers.items(), key=lambda item: item[1], reverse=True)


def calculate_risk(name):
    """Risk = 100 - Stability - Economy/2 - Military/4, clamped to 0-100."""
    stats = get_country_stats(name)
    economy = stats["economy"]
    military = stats["military"]
    stability = stats["stability"]
    raw_risk = 100 - stability - economy / 2 - military / 4
    return max(0, min(100, round(raw_risk)))

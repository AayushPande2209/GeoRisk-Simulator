"""Country power calculations for the GeoRisk Simulator."""

from countries import get_country_names, get_country_stats


def calculate_power(name):
    stats = get_country_stats(name)
    return stats["economy"] + stats["military"] + stats["stability"] + stats["technology"]


def get_power_rankings():
    powers = {name: calculate_power(name) for name in get_country_names()}
    return sorted(powers.items(), key=lambda item: item[1], reverse=True)

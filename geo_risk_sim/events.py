"""Random geopolitical events for the GeoRisk Simulator.

Each event is a dict with a "name" and an "effects" dict mapping a
stat name to the amount it changes by (positive or negative).
"""

import random

EVENTS = [
    {"name": "Economic Boom", "effects": {"economy": 8}},
    {"name": "Recession Hits", "effects": {"economy": -8}},
    {"name": "Military Coup Attempt", "effects": {"stability": -15, "military": 5}},
    {"name": "Trade Agreement Signed", "effects": {"economy": 6, "stability": 3}},
    {"name": "Border Skirmish", "effects": {"military": -5, "stability": -5}},
    {"name": "Tech Breakthrough", "effects": {"technology": 10}},
    {"name": "Cyber Attack Cripples Infrastructure", "effects": {"technology": -8, "stability": -4}},
    {"name": "Natural Disaster Strikes", "effects": {"economy": -6, "stability": -6, "population": -2}},
    {"name": "Population Boom", "effects": {"population": 5}},
    {"name": "Pandemic Outbreak", "effects": {"population": -8, "economy": -5}},
    {"name": "Foreign Investment Surge", "effects": {"economy": 7}},
    {"name": "Corruption Scandal", "effects": {"stability": -10}},
    {"name": "Successful Diplomatic Summit", "effects": {"stability": 6}},
    {"name": "Arms Race Escalation", "effects": {"military": 8, "economy": -3}},
    {"name": "Research Grant Windfall", "effects": {"technology": 6, "economy": 2}},
    {"name": "Civil Unrest", "effects": {"stability": -12}},
    {"name": "Military Modernization Program", "effects": {"military": 7}},
    {"name": "Drought Damages Agriculture", "effects": {"economy": -4, "population": -1}},
    {"name": "Global Trade Boycott", "effects": {"economy": -7}},
    {"name": "Space Program Success", "effects": {"technology": 9, "stability": 2}},
    {"name": "Terrorist Attack", "effects": {"stability": -8, "military": 3}},
    {"name": "Energy Crisis", "effects": {"economy": -5, "stability": -3}},
]


def get_random_event():
    return random.choice(EVENTS)

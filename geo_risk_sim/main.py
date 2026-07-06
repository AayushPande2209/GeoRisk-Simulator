"""GeoRisk Simulator - entry point.

Shows a title screen, lets the player pick a country, and then runs the
main menu loop: viewing stats, improving them, advancing the year with
random events, and checking world rankings.
"""

from countries import (
    apply_stat_delta,
    get_country_names,
    get_country_stats,
    increase_stat,
)
from events import get_random_event
from calculations import calculate_risk, get_power_rankings

START_YEAR = 2025
END_YEAR = 2045
SEPARATOR = "=" * 44

TITLE_ART = r"""
  ____                _____  _     _      _____ _
 / ___| ___  ___     |  __ \(_)   | |    / ____(_)
| |  _ / _ \/ _ \    | |__) |_ ___| | __| (___  _ _ __ ___
| |_| |  __/ (_) |   |  _  /| / __| |/ /\___ \| | '_ ` _ \
 \____|\___|\___/    | | \ \| \__ \   < ____) | | | | | | |
                     |_|  \_\_|___/_|\_\_____/|_|_| |_| |_|

                GEORISK SIMULATOR
"""


def show_title_screen():
    """Print the ASCII art title screen."""
    print(TITLE_ART)


def print_header(title):
    """Print a consistent section header used across every screen."""
    print(f"\n{SEPARATOR}")
    print(f" {title}")
    print(SEPARATOR)


def prompt_choice(prompt_text, valid_choices):
    """Prompt until the user enters one of valid_choices, then return it.

    Centralizes input validation so no menu can ever receive or act on
    a value outside its expected set - invalid input just re-prompts.
    """
    while True:
        choice = input(prompt_text).strip()

        if choice in valid_choices:
            return choice

        options = ", ".join(sorted(valid_choices))
        print(f"Invalid input. Please enter one of: {options}")


def choose_country():
    """Display country options and return the player's chosen country name."""
    names = get_country_names()

    print_header("CHOOSE YOUR COUNTRY")
    for index, name in enumerate(names, start=1):
        print(f"  {index}. {name}")
    print(SEPARATOR)

    valid_choices = {str(i) for i in range(1, len(names) + 1)}
    choice = prompt_choice("Enter the number of your choice: ", valid_choices)
    return names[int(choice) - 1]


def print_country_stats(name):
    """Print a country's stats, including Risk Score, in a formatted report."""
    stats = get_country_stats(name)
    risk = calculate_risk(name)

    print_header(f"{name} - COUNTRY REPORT")
    print(f"  Economy:    {stats['economy']:>3}")
    print(f"  Military:   {stats['military']:>3}")
    print(f"  Stability:  {stats['stability']:>3}")
    print(f"  Technology: {stats['technology']:>3}")
    print(f"  Population: {stats['population']:>5} million")
    print(SEPARATOR)
    print(f"  Risk Score: {risk:>3} / 100")
    print(SEPARATOR)


def show_menu(year):
    """Print the main menu with the current year as a header."""
    print_header(f"YEAR {year}")
    print("  1. View Country")
    print("  2. Improve Economy")
    print("  3. Build Military")
    print("  4. Increase Stability")
    print("  5. Research Technology")
    print("  6. Advance Year")
    print("  7. World Rankings")
    print("  8. Quit")
    print(SEPARATOR)


MENU_CHOICES = {"1", "2", "3", "4", "5", "6", "7", "8"}


def get_menu_choice():
    """Prompt for and return a validated main menu choice."""
    return prompt_choice("Enter your choice (1-8): ", MENU_CHOICES)


STAT_ACTIONS = {
    "2": ("economy", "Economy"),
    "3": ("military", "Military"),
    "4": ("stability", "Stability"),
    "5": ("technology", "Technology"),
}


def apply_stat_action(country, choice):
    """Increase the stat mapped to the given menu choice by 5 points."""
    stat_key, stat_label = STAT_ACTIONS[choice]
    increase_stat(country, stat_key, 5)
    print(f"  {stat_label} increased by 5.")


def apply_event(country):
    """Apply a random event's effects to country and print the result."""
    event = get_random_event()

    print(f"  Event: {event['name']}")
    for stat, delta in event["effects"].items():
        actual_change = apply_stat_delta(country, stat, delta)
        sign = "+" if actual_change >= 0 else ""
        print(f"    {stat.capitalize()}: {sign}{actual_change}")
    print(SEPARATOR)


def advance_year(country, year):
    """Advance the year by one, trigger a random event, and return it."""
    year += 1
    print_header(f"ADVANCING TO YEAR {year}")
    apply_event(country)
    return year


def show_world_rankings(country):
    """Print every country ranked by Power Score and the player's rank."""
    rankings = get_power_rankings()

    print_header("WORLD POWER RANKINGS")
    player_rank = None
    for rank, (name, power) in enumerate(rankings, start=1):
        marker = "  <-- YOU" if name == country else ""
        print(f"  {rank}. {name:<15} Power: {power:>3}{marker}")
        if name == country:
            player_rank = rank
    print(SEPARATOR)
    print(f"  Your ranking: {player_rank} of {len(rankings)}")
    print(SEPARATOR)


def run_game_loop(country):
    """Run the main menu loop until the player quits or the simulation ends."""
    year = START_YEAR
    playing = True

    while playing:
        show_menu(year)
        choice = get_menu_choice()

        if choice == "1":
            print_country_stats(country)
        elif choice in STAT_ACTIONS:
            apply_stat_action(country, choice)
        elif choice == "6":
            year = advance_year(country, year)
            if year >= END_YEAR:
                print_header(f"YEAR {END_YEAR} REACHED")
                print("  The simulation has ended.")
                print(SEPARATOR)
                playing = False
        elif choice == "7":
            show_world_rankings(country)
        elif choice == "8":
            print("\nThanks for playing GeoRisk Simulator. Goodbye!")
            playing = False


def main():
    """Run the GeoRisk Simulator, exiting cleanly on Ctrl+C/Ctrl+D."""
    try:
        show_title_screen()
        chosen_country = choose_country()
        run_game_loop(chosen_country)
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting GeoRisk Simulator. Goodbye!")


if __name__ == "__main__":
    main()

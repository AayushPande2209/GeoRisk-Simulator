"""GeoRisk Simulator - entry point.

This is the initial version of the project. It shows a title screen,
lets the player pick a country, prints that country's stats, and exits.
No gameplay logic is implemented yet.
"""

from countries import get_country_names, get_country_stats, increase_stat, apply_stat_delta
from events import get_random_event
from calculations import get_power_rankings

START_YEAR = 2025
END_YEAR = 2045

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
    print(TITLE_ART)


def choose_country():
    names = get_country_names()

    print("Choose a country to play as:")
    for index, name in enumerate(names, start=1):
        print(f"  {index}. {name}")

    while True:
        choice = input("Enter the number of your choice: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return names[int(choice) - 1]

        print("Invalid choice. Please enter a valid number from the list.")


def print_country_stats(name):
    stats = get_country_stats(name)

    print(f"\n--- {name} ---")
    print(f"Economy:    {stats['economy']}")
    print(f"Military:   {stats['military']}")
    print(f"Stability:  {stats['stability']}")
    print(f"Technology: {stats['technology']}")
    print(f"Population: {stats['population']} million")


def show_menu(year):
    print(f"\nYear: {year}")
    print("1. View Country")
    print("2. Improve Economy")
    print("3. Build Military")
    print("4. Increase Stability")
    print("5. Research Technology")
    print("6. Advance Year")
    print("7. World Rankings")
    print("8. Quit")


def get_menu_choice():
    return input("Enter your choice (1-8): ").strip()


STAT_ACTIONS = {
    "2": ("economy", "Economy"),
    "3": ("military", "Military"),
    "4": ("stability", "Stability"),
    "5": ("technology", "Technology"),
}


def apply_stat_action(country, choice):
    stat_key, stat_label = STAT_ACTIONS[choice]
    increase_stat(country, stat_key, 5)
    print(f"{stat_label} increased by 5.")


def apply_event(country):
    event = get_random_event()

    print(f"\nEvent: {event['name']}")
    for stat, delta in event["effects"].items():
        actual_change = apply_stat_delta(country, stat, delta)
        sign = "+" if actual_change >= 0 else ""
        print(f"  {stat.capitalize()}: {sign}{actual_change}")


def advance_year(country, year):
    year += 1
    print(f"\n--- Advancing to {year} ---")
    apply_event(country)
    return year


def show_world_rankings(country):
    rankings = get_power_rankings()

    print("\n--- World Power Rankings ---")
    player_rank = None
    for rank, (name, power) in enumerate(rankings, start=1):
        marker = "  <-- YOU" if name == country else ""
        print(f"  {rank}. {name} - Power: {power}{marker}")
        if name == country:
            player_rank = rank

    print(f"\nYour ranking: {player_rank} of {len(rankings)}")


def run_game_loop(country):
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
                print(f"\nYear {END_YEAR} reached. The simulation has ended.")
                playing = False
        elif choice == "7":
            show_world_rankings(country)
        elif choice == "8":
            print("\nThanks for playing GeoRisk Simulator. Goodbye!")
            playing = False
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


def main():
    show_title_screen()
    chosen_country = choose_country()
    run_game_loop(chosen_country)


if __name__ == "__main__":
    main()

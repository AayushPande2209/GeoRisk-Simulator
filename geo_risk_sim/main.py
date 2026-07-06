"""GeoRisk Simulator - entry point.

This is the initial version of the project. It shows a title screen,
lets the player pick a country, prints that country's stats, and exits.
No gameplay logic is implemented yet.
"""

from countries import get_country_names, get_country_stats

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


def main():
    show_title_screen()
    chosen_country = choose_country()
    print_country_stats(chosen_country)
    print("\nThanks for playing GeoRisk Simulator. Goodbye!")


if __name__ == "__main__":
    main()

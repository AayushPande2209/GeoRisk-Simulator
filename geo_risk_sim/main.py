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


def show_menu(year):
    print(f"\nYear: {year}")
    print("1. View Country")
    print("2. Improve Economy")
    print("3. Build Military")
    print("4. Increase Stability")
    print("5. Research Technology")
    print("6. Advance Year")
    print("7. Quit")


def get_menu_choice():
    return input("Enter your choice (1-7): ").strip()


def run_game_loop(country):
    year = 2025
    playing = True

    while playing:
        show_menu(year)
        choice = get_menu_choice()

        if choice == "1":
            print_country_stats(country)
        elif choice in ("2", "3", "4", "5", "6"):
            print("Feature coming soon.")
        elif choice == "7":
            print("\nThanks for playing GeoRisk Simulator. Goodbye!")
            playing = False
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


def main():
    show_title_screen()
    chosen_country = choose_country()
    run_game_loop(chosen_country)


if __name__ == "__main__":
    main()

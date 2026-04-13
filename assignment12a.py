"""
Name: Hernan Ramoz
Course: ADD-100
Assignment: 12A - The Configurable Menu & Auditor

Description:
This program reads a menu from a text file.
It separates the data into categories.
Then it prints each category and its items.

The program also uses try/except to avoid crashing
if the file is not found.
"""

def read_menu():
    menu = {}

    try:
        file = open("menu_config.txt", "r")

        for line in file:
            line = line.strip()
            parts = line.split(":")
            category = parts[0]
            items = parts[1]
            menu[category] = items

        file.close()

    except FileNotFoundError:
        print("Error: file not found")

    return menu


def print_menu(menu):
    print("MENU:\n")

    for category in menu:
        print(category)

        items = menu[category].split(",")

        for item in items:
            print("-", item.strip())

        print()


def main():
    menu = read_menu()
    print_menu(menu)


main()
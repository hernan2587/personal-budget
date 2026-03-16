"""
Name: Hernan Ramoz
Course: ADD 100
Assignment: Smoothie Sprint

Checklist:
[x] Header Docstring included.
[x] Global constants BASES and FRUITS defined as tuples.
[x] Professional function get_price(size) returns a float.
[x] Professional function blend(size, base, fruit, scoops) for output.
[x] main() function handles try/except for scoops (int).
[x] main() calls both functions correctly.
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


def get_price(size):
    """Return the smoothie price based on size."""
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00


def blend(size, base, fruit, scoops):
    """Print the final smoothie order."""
    print("\n----- Smoothie Order -----")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")


def main():
    print("Welcome to Smoothie Bar")

    choice_size = input("Enter size (Small/Medium/Large): ").title().strip()
    choice_base = input("Choose a base: ").title().strip()
    choice_fruit = input("Choose a fruit: ").title().strip()

    try:
        scoops = int(input("How many scoops? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1.")
        scoops = 1

    total = get_price(choice_size)
    blend(choice_size, choice_base, choice_fruit, scoops)

    print(f"Total Price: ${total:.2f}")


main()
"""
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE

1. Header Docstring included.
2. Global constant TOPPINGS defined as a tuple in ALL_CAPS.
3. Function make_pizza defines 4 parameters.
4. make_pizza uses a DEFAULT value for is_delivery.
5. main() displays the global toppings list to the user.
6. main() calls the function using KEYWORD ARGUMENTS.

Hernan Ramoz
Course ADD-100

"""

# GLOBAL CONSTANT
TOPPINGS = ("pepperoni", "cheese", "mushrooms", "ham")

def make_pizza(customer, size, topping, is_delivery=False):
    print(f"\n--- ORDER ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Delivery: {is_delivery}")

def main():
    customer = input("Name: ").title()
    size = input("Size (small/medium/large): ")

    print("Available toppings:", TOPPINGS)
    topping = input("Choose topping: ")

    delivery_input = input("Delivery? (yes/no): ").lower()
    is_delivery = True if delivery_input == "yes" else False

    make_pizza(customer=customer, size=size, topping=topping, is_delivery=is_delivery)

main()







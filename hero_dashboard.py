"""
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD

[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
"""

OFFICE_NAME = "McHenry College Office"
TAX_RATE = 0.05


def process_expenses(item_name, price, quantity):
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    total_expense = subtotal + tax

    if total_expense > 1000:
        summary = f"{item_name} expense exceeds $1000"
    else:
        summary = f"{item_name} expense is within budget"

    return total_expense, summary


def main():
    item_name = input("Enter item name: ")

    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    final_cost, summary_text = process_expenses(
        item_name=item_name,
        price=price,
        quantity=quantity
    )

    print(f"\nOffice Name: {OFFICE_NAME}")
    print(f"Final Cost: ${final_cost:.2f}")
    print(f"Summary: {summary_text}")


main()     
        



    





"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""
#GLOBAL CONSTANTS
OFFICE_NAME = "The Office Supply Store"
TAX_RATE = 0.05

def process_expenses(item_name, price, quantity):
    """Calculates total expenses and determines if it exceeds $1000"""
    total_expense = price * quantity * (1 + TAX_RATE)
    if total_expense > 1000:
        return total_expense, f"{item_name} expense exceeds $1000"
    else:
        return total_expense, f"{item_name} expense is within budget"
    
def main():
    iten_name = input("Enter item name: ")

    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))

        final_total, summary = process_expenses(item_name=iten_name, price=price, quantity=quantity)

        print("Office Name:", OFFICE_NAME)
        print("Final Total:", final_total)
        print("Summary:", summary)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    if __name__== "__main":
        main()        
        



    





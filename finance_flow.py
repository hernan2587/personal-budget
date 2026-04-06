"""
Name: Hernan Ramoz
Course: ADD 100
Project: Finance Flow

Description:
This program helps users understand their monthly finances.
It asks for income, expenses, and debt payments.
Then it calculates how much money is left.
"""

# Global Constants
WELCOME_MESSAGE = "Welcome to Finance Flow"
PROGRAM_MESSAGE = "This program helps you understand your monthly finances.\n"
ERROR_MESSAGE = "Invalid input. Please enter numbers only."


def show_welcome():
    print(WELCOME_MESSAGE)
    print(PROGRAM_MESSAGE)


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print(ERROR_MESSAGE)


def get_income():
    income = get_number("Enter your monthly income: ")
    return income


def get_expenses():
    
    expenses = get_number("Enter your monthly expenses: ")
    return expenses


def get_debt():
    debt = get_number("Enter your monthly debt payments: ")
    return debt


def calculate_balance(income, expenses, debt=0):
    balance = income - expenses - debt
    return balance


def show_summary(balance, title="Financial Summary"):
    print("\n-----", title, "-----")
    print("Money left after expenses and debt:", balance)

    if balance < 0:
        print("Warning: You are spending more than you earn.")
    elif balance == 0:
        print("You have no money left this month.")
    else:
        print("Good job! You still have money left.")


def save_to_file(balance):
    with open("finance_log.txt", "a") as file:
        file.write("Balance: " + str(balance) + "\n")


def main():
    show_welcome()

    income = get_income()
    expenses = get_expenses()
    debt = get_debt()

    balance = calculate_balance(income=income, expenses=expenses, debt=debt)

    show_summary(balance=balance)
    save_to_file(balance)


main()
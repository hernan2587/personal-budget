"""
Name: Hernan Ramoz
Course: ADD 100
Project: Finance Flow

Description:
This program helps users understand their monthly finances.
It asks for income, expenses, and debt payments.
Then it calculates how much money is left.
"""

def show_welcome():
    print("Welcome to Finance Flow")
    print("This program helps you understand your monthly finances.\n")


def get_income():
    income = float(input("Enter your monthly income: "))
    return income


def get_expenses():
    expenses = float(input("Enter your monthly expenses: "))
    return expenses


def get_debt():
    debt = float(input("Enter your monthly debt payments: "))
    return debt


def calculate_balance(income, expenses, debt):
    balance = income - expenses - debt
    return balance


def show_summary(balance):
    print("\n----- Financial Summary -----")
    print("Money left after expenses and debt:", balance)

    if balance < 0:
        print("Warning: You are spending more than you earn.")
    elif balance == 0:
        print("You have no money left this month.")
    else:
        print("Good job! You still have money left.")


def main():
    show_welcome()

    income = get_income()
    expenses = get_expenses()
    debt = get_debt()

    balance = calculate_balance(income, expenses, debt)

    show_summary(balance)


main()
"""
Name: Hernan Ramoz
Course: ADD 100
Project: Finance Flow (Sprint 2 - Stub Version)

Description:
This program is a basic structure of Finance Flow.
It shows how data moves between functions.
"""

def show_welcome():
    print("Welcome to Finance Flow")

def get_income():
    # TODO: ask user for income
    return 0

def get_expenses():
    # TODO: ask user for expenses
    return 0

def get_debt():
    # TODO: ask user for debt
    return 0

def calculate_balance(income, expenses, debt):
    # TODO: calculate real balance
    return 0

def show_summary(balance):
    # TODO: show real summary
    print("Summary will be shown here")

def main():
    show_welcome()

    income = get_income()
    expenses = get_expenses()
    debt = get_debt()

    balance = calculate_balance(income, expenses, debt)

    show_summary(balance)

main()
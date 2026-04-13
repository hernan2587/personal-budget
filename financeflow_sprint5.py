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


def read_menu():
    income_label = "monthly income"
    expense_label = "monthly expenses"
    debt_label = "monthly debt payments"

    try:
        file = open("finance_menu.txt", "r")

        for line in file:
            line = line.strip()
            parts = line.split(":")

            if parts[0] == "INCOME_LABEL":
                income_label = parts[1].strip()

            elif parts[0] == "EXPENSE_LABEL":
                expense_label = parts[1].strip()

            elif parts[0] == "DEBT_LABEL":
                debt_label = parts[1].strip()

        file.close()

    except FileNotFoundError:
        print("Error: file not found")

    return income_label, expense_label, debt_label


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print(ERROR_MESSAGE)


def get_income(label):
    income = get_number("Enter your " + label + ": ")
    return income


def get_expenses(label):
    expenses = get_number("Enter your " + label + ": ")
    return expenses


def get_debt(label):
    debt = get_number("Enter your " + label + ": ")
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


def save_report(balance):
    with open("finance_report.txt", "w") as file:
        file.write("Financial Report\n")
        file.write("--------------------\n")
        file.write("Balance: " + str(balance) + "\n")

        if balance < 0:
            file.write("Warning: You are spending more than you earn.\n")
        elif balance == 0:
            file.write("You have no money left this month.\n")
        else:
            file.write("Good job! You still have money left.\n")


def main():
    show_welcome()

    income_label, expense_label, debt_label = read_menu()

    income = get_income(income_label)
    expenses = get_expenses(expense_label)
    debt = get_debt(debt_label)

    balance = calculate_balance(income=income, expenses=expenses, debt=debt)

    show_summary(balance=balance)
    save_to_file(balance)
    save_report(balance)


main()
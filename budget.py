"""
Assignment 3A: Number Formatting & Math
Name: Hernan Ramoz
Description:
This program calculates a personal monthly budget by asking the user
for income and expenses, then computes the total expenses and the
percentage of income spent.
"""

# 1. Get Input
gross_pay = float(input("Enter monthly Gross pay: $"))

rent = float(input("Enter monthly rent: $"))
insunrance = float(input("Enter monthly insurance: $"))
gas = float(input("Enter monthly gas: $"))
phone = float(input("Enter monthly phone: $"))
gym =float(input("Enter monthly gym: $"))

# 2. Total Exoenses, remaining, and income

total_expenses = rent + insunrance + gas + phone + gym
remaining_balance = gross_pay - total_expenses
percent_spent = (total_expenses / gross_pay) * 100

print("Monthly Budget Summary")
print("Total Expenses: $", format(total_expenses, ".2f"))
print("Remaining Balance: $", format(remaining_balance, ".2f"))
print("Percentage Spent: ", format(percent_spent, ".2f"), "%")





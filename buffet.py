"""
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 2026-01-29
NAME: Hernan Ramoz
FILE: buffet.py

DESCRIPTION:
This program asks the user for their age and calculates the buffet price
using if/elif/else based on the assignment pricing rules. It prints the
final price formatted as currency.
"""

# 1) Ask for age (convert to int)
age = int(input("Enter your age: "))

# 2) Pricing logic using if/elif/else
if age < 1:
    price = 0.00
elif age <= 11:
    price = float(age) * 1.00
elif age <= 64:
    price = 16.95
else:
    price = 12.95

# 3) Print final price formatted as currency
print(f"${price:.2f}")
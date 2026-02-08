"""

Assignment 4A: Boolean Logic - The Logic Gate
Course: ADD-100
Name: Hernan Ramoz
Description: Program that takes two integers and performs boolean logic tests.


#[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
"""


# 1.  Ask user for two integers (num1 and num2).

num1 = int(input("Enter integer #1: "))
num2 = int(input("Enter integer #2: "))

# 2. Perform 6 logical checks.

"""
Logic Gate Assignment
Name: Hernan Ramoz
"""

# Ask user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print("\n--- Logical Checks ---")

# 1) Both > 0
if num1 > 0 and num2 > 0:
    print("Both > 0: True")
else:
    print("Both > 0: False")

# 2) Both > 100
if num1 > 100 and num2 > 100:
    print("Both > 100: True")
else:
    print("Both > 100: False")

# 3) Either Even
if num1 % 2 == 0 or num2 % 2 == 0:
    print("Either Even: True")
else:
    print("Either Even: False")

# 4) Either < 100
if num1 < 100 or num2 < 100:
    print("Either < 100: True")
else:
    print("Either < 100: False")

# 5) Not Equal
if num1 != num2:
    print("Not Equal: True")
else:
    print("Not Equal: False")

# 6) Not Zero (both not zero)
if num1 != 0 and num2 != 0:
    print("Not Zero: True")
else:
    print("Not Zero: False")

print("\n--- Categorize num1 ---")

# Categorize num1 (Positive / Negative / Zero)
if num1 > 0:
    print("num1 is Positive.")
elif num1 < 0:
    print("num1 is Negative.")
else:
    print("num1 is Zero.")
                        




    







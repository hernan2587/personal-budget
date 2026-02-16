"""

Assignment 5B: The ATM Logic Task
ADD-100: Hernan Ramoz
Simulates an ATM system using match-case.
Allow user to check balance, deposit, withdraw, transfer, and exit.
Date: 2/12/2026

"""

balance = 1000.00

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Choose an option: ")

    match choice:
        case "1":
            print(f"Your balance is: ${balance:.2f}")

        case "2":
            amount = input("Enter deposit amount: ")

            if amount.replace(".", "", 1).isdigit():
                amount = float(amount)

                if amount > 0:
                    balance += amount
                    print(f"Deposit successful. New balance: ${balance:.2f}")
                else:
                    print("Deposit must be positive.")
            else:
                print("Invalid amount. Please enter a number.")

        case "3":
            amount = input("Enter withdrawal amount: ")

            if amount.replace(".", "", 1).isdigit():
                amount = float(amount)

                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"Withdrawal successful. New balance: ${balance:.2f}")
                    else:
                        print("Insufficient funds. Cannot overdraft.")
                else:
                    print("Withdrawal must be positive.")
            else:
                print("Invalid amount. Please enter a number.")

        case "4":
            amount = input("Enter transfer amount: ")

            if amount.replace(".", "", 1).isdigit():
                amount = float(amount)

                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"Transfer successful. New balance: ${balance:.2f}")
                    else:
                        print("Insufficient funds. Cannot overdraft.")
                else:
                    print("Transfer must be positive.")
            else:
                print("Invalid amount. Please enter a number.")

        case "5":
            print("Goodbye!")
            break

        case _:
            print("Invalid selection.")
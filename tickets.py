"""
ASSIGNMENT 6A: TICKET SALES
Hernan Ramoz
ADD-100

1. Create a list of 20 seats (numbered 1-20).
2. Display the list of available seats.
3. Ask user for a seat number (0 to quit).
4. Remove the selected seat from the list.
5. Handle invalid inputs (seat taken or doesn't exist).
6. Repeat until user quits or seats are empty.
"""

seats = list(range(1, 21))  # 1 to 20

while len(seats) > 0:
    print("\nAvailable seats:", seats)

    choice = input("Pick a seat number (1-20) or 0 to quit: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 0:
        print("Goodbye!")
        break

    if choice in seats:
        seats.remove(choice)
        print(f"Seat {choice} sold!")
    else:
        print("That seat is gone or doesn't exist.")

if len(seats) == 0:
    print("All seats sold out!")

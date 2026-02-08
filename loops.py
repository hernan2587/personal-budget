"""
Name: Hernan
Course: ADD-100
Assignment: The Nag & The Song

Description:
This program uses while and for loops.
It asks the user "Are we there yet?" until the user types "yes".
Then it counts from 99 down to 1 and prints the bottles of beer song.
"""

nagging = True

while nagging:
    answer = input("Are we there yet? ")
    if answer == "yes":
        nagging = False

for bottles in range(99, 0, -1):
    print(f"{bottles} bottles of beer on the wall!")


"""

Assignment 5A: Input Validation
Name: Hernan Ramoz
Course: ADD-100

"""

first_name = input("Enter first name: ")

while first_name == "":
    print("   Error: First name cannot be blank.")
    first_name = input("Enter first name: ")

last_name = input("Enter last name: ")

while last_name == "":
    print("   Error: Last name cannot be blank. ")
    last_name = input("Enter last name: " )

chaperone = input("Chaperone? Y/N ").upper()
while chaperone != "Y" and chaperone != "N":
    print("❌ Error: Please enter Y or N.")
    chaperone = input("Chaperone? (Y/N): ").upper()

phone = input("Enter phone number: ")

while phone == "":
    print("❌ Error: Phone number cannot be blank.")
    phone = input("Enter phone number: ")

while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break
        else:
            print("❌ Error: Must be at least 1 ticket.")
    except ValueError:
        print("❌ Error: Please enter a NUMBER.")

print(f"\n✅ Registration complete for {first_name} {last_name}.")




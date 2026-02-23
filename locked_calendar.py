"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""
# This is a constant tuple that contains the names of the months in a calendar year.
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") 
# The following code attempts to modify the MONTHS tuple, which is immutable and will raise a TypeError.
try:
    MONTHS[0] = "Jan"  # This line will raise a TypeError because tuples cannot be modified after they are created.
except TypeError as e:
    print("Error: Cannot modify a tuple. Tuples are immutable, meaning their contents cannot be changed after they are created.")
    print(f"TypeError: {e}")    
# The following code uses a for loop to display each month in the MONTHS tuple.
for month in MONTHS:
    print(month)    



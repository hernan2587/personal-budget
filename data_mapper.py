"""
ASSIGNMENT 8A - OPTION A - NATO TRANSLATOR
Hernan Ramoz
Add-100

Checklist:
[X] Header Docstring included
[X] NATO_ALPHABET constant dictionary (A-Z)
[X] Program takes a word and uppercases it
[X] Program loops through letters
[X] Try/Except handles errors
"""

NATO_ALPHABET = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
}

word = input("Enter word to spell: ").upper()

for letter in word:
    try:
        print(NATO_ALPHABET[letter])
    except KeyError:
        print(letter)

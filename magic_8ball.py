"""
ASSIGNMENT 7B: MAGIC 8 BALL
Author: Hernan
Course: ADD 100
Description: A digital oracle that answers questions.
"""

import random

RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Definitely",
    "Very doubtful",
    "Without a doubt",
    "Cannot predict now"
)

print("Welcome to the Digital Oracle!")

while True:
    question = input("Ask a question (or type quit to exit): ")

    # Clean the input
    clean_question = question.strip().lower()

    # Exit condition
    if clean_question == "quit":
        print("Goodbye!")
        break

    # Get random answer
    answer = random.choice(RESPONSES)


    print(answer)
    
     
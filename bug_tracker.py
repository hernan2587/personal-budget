"""
ASSIGNMENT 11A REVISED: BUG TRACKER
ADD-100
Hernan Ramoz 
This program allows the user to log bugs by entering basic information.
It saves each bug with a timestamp in the text file.
 
"""

from datetime import datetime


def main():

    while True:

        choice = input("Type 'log' to add bug or 'quit' to stop: ")

        if choice == "quit":
            print("Done")
            break

        if choice == "log":

            file_name = input("File name: ")
            description = input("Error: ")
            priority = input("Priority: ")

            # get time
            time_now = datetime.now()

            # simple dictionary
            bug = {
                "time": time_now,
                "file": file_name,
                "error": description,
                "priority": priority
            }

            # save to file
            file = open("bug_log.txt", "a")

            file.write(str(bug))
            file.write("\n")

            file.close()

            print("Saved")

        else:
            print("Wrong option")


main()
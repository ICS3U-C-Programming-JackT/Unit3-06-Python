#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 18th, 2025

# Random number guessing program in python

import random


def main():

    # Create a random number
    randomNum = int(random.randrange(1, 10))
    print("For testing purposes, heres the random number: ", randomNum)

    correct = False
    #Try catch to verify that the user is 
    #entering a valid number, checking string>int
    try:
        userNumber = int(input("Enter a number between 1 and 9: "))
        if userNumber == randomNum:
            #Set correct to true, ensuring we dont loop again
            correct = True
            print("YOU GUESSED RIGHT!!! 🥳")

        # Check if number is higher or lower than the program number
        if userNumber > randomNum or userNumber < randomNum:
            print("Aww, not the right answer, sorry!")

        # Check if number is within the range
        if userNumber > 9 or userNumber < 1:
            print("Please enter a number within the proper range (1-9)")
    except:
        print("Please enter a valid number next time!")
    finally:
        if correct == False:
            print("Lets try that again")
            main()  # Fire main function to restart


if __name__ == "__main__":
    # Fire main function to begin
    main()

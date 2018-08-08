# The user keeps a number between 0 and 100 in mind, and the program guesses based on the user's feedback: high, low, correct.

import random

def GuessingGame():

    again_flag = 1  # flag for playing again

    while again_flag == 1:
        count = 1
        wrong = 1

        lowest = 0
        highest = 100

        print("Pick a number in range 0 <= x <= 100 and the program will attempt to guess it, for every guess give it some feedback.")
        print("(Play) or (quit)? ")

        userIn = input()

        low = "low"
        yes = "correct"
        high = "high"

        if(userIn == "quit"):
            break

        # first guess
        pGuess = random.randint(0,100)

        print("Guess " + str(count) + ": " + str(pGuess) + ", is this (low) (correct) (high)? ")
        quit = 0

        while wrong == 1:

            userIn = input()

            if(userIn == "quit"):

                break

            elif (userIn == yes):
                wrong = 0
            elif (userIn == high):

                #check against prev highest guess
                if pGuess < highest:
                    highest = pGuess
                #print("Highest " + str(highest))
                pGuess = (lowest + highest) // 2  # floor divide


            elif (userIn == low):

                if pGuess > lowest:
                    lowest = pGuess
                #print("Lowest " + str(lowest))
                pGuess = int((lowest + highest) // 2)
                if (pGuess > 100):
                    pGuess = 100

            print("Low " + str(lowest) + " High " + str(highest))

            print("Guess " + str(count) + ": " + str(pGuess) + ", is this (low) (correct) (high) (quit)? ")
            count += 1

        if wrong == 0:
            print("Took " + str(count) + " guess(es) to pick " + str(pGuess))

        userIn = input("Would you like to (play) again or (exit)? ")
        if userIn == "exit":
            again_flag = 0

GuessingGame()

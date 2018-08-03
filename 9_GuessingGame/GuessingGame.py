# Generate a random number between 1 to 9 and the user will guess
# Feedback is too low, high, or got it.
import random

def GuessingGame():

    while True:

        randGen = random.randint(1, 9)
        while True:
            guessIn = input("Guess a number from 1 to 9 that you think random has generated: ")

            if (int(guessIn) == randGen):
                print("You picked the correct number!")
                break
            elif (int(guessIn) < randGen):
                print ("Your guess is too low.")
            else:
                print("Your guess is too high.")

        quit = input("Would you like to play again? (anything / N) ")

        if (quit == "N"):
            break

GuessingGame()

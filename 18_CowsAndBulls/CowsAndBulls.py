# Generate a 4 digit number and the user takes guesses. If the user guesses a number in the correct spot it is called a "cow", if the User
# guesses a correct number but in the incorrect position then it is called a bull

# I will also indicate which positions are cows and bulls

import random

def CowsAndBulls():
    print("Cow = correct number and location; Bull = correct number, but wrong location.\n")
    print("Duplicates are allowed.")

    # playAgain = 1
    #while playAgain == 1:
    #can do it by range (randint) or genereate each digit seperately (convert to string and concat)
    generated = str(random.randint(0000, 9999))
    resultList = []
    # inner loop start
    # loop until user guesses correct
    while True:
        resultList[:] = [] # empty the list
        count = 0
        userGuess = str(input("What 4 digit number would you like to guess? "))

        for x in range(len(generated)):
            # check the current location
            if(userGuess[x] == generated[x]):
                resultList.append("Cow")
                count += 1
            # if number not in current location, check if in the others
            elif userGuess[x] in generated:

                resultList.append("Bull")
                #for y in range(len(generated)):
                #    if(userGuess[x] == generated[y]):
                #        resultList.append("Bull")
            else:
                resultList.append("Wrong")

        print (*resultList, sep=', ')
        if count == 4:
            print("You guessed right!\n")
            break

    #if again = "quit":
        #playAgain = 0
    # ------ inner loop end

CowsAndBulls()

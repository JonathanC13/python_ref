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

    cow = "Cow"
    bull = "Bull"
    cowbull = "Cow/Bull"
    wrong = "Wrong"

    # inner loop start
    # loop until user guesses correct
    guesses = 0
    while True:

        generated = "5996"
        prevList = resultList[:]    # do copy, not just same reference
        count = 0
        userGuess = str(input("What 4 digit number would you like to guess or (answer)? "))

        if(userGuess == "answer"):
            print("The answer is: " + generated)
            break

        guesses += 1

        for x in range(len(generated)):
            # check the current location
            if(userGuess[x] == generated[x]):

                resultList.append(cow)
                count += 1

            # if number not in current location, check if in the others
            elif userGuess[x] in generated:

                resultList.append(bull)

                #for y in range(len(generated)):
                #    if(userGuess[x] == generated[y]):
                #        resultList.append("Bull")
            else:
                resultList.append(wrong)
        print("org: " )
        print(resultList)

        for twice in range(1):
            # after first run do clean up of duplicates and false bulls since some may point to a cow. Misleading
            for pos in range(len(resultList)):
                print("===================")
                marked_cow = 1
                if resultList[pos] == bull:
                    # just check whole range, something went wrong with pos + 1
                    a = pos + 1;
                    if(a >= len(resultList)-1):
                        a = len(resultList)-1

                    for check in range(a, len(resultList)):
                        # first check if val matches
                        if userGuess[pos] == generated[check]:
                            # if match value, check if not marked as cow it is confirmed that this is a bull
                            if resultList[check] != cow and resultList[check] != cowbull:
                                marked_cow = 0

                                break

                    # if all same values are marked cow, this bull is not a bull
                    if marked_cow == 1:
                        resultList[pos] = wrong

                # check if cow value can be somewhere else
                elif resultList[pos] == str(cow):

                    for chk in range(pos+1, len(resultList)):

                        if userGuess[pos] == generated[chk]:

                            if (resultList[chk] != cow) and (resultList[chk] != cowbull):
                                marked_cow = 0

                                break
                    # if there are cow values in other places not marked cow, then indicate /bull
                    if marked_cow == 0:

                        resultList[pos] = cowbull

                elif resultList[pos] == cowbull:

                    for ck in range(pos+1, len(resultList)):
                        if userGuess[pos] == generated[ck]:
                            # if this cow bull sees that other same value position is not marked cow, then this is still a cow/bull
                            if resultList[ck] != cow and resultList[ck] != cowbull:

                                marked_cow = 0
                                break

                    # if all marked then it changes to cow
                    if marked_cow == 1:

                        resultList[pos] == cow

        # outside for
        print (*resultList, sep=', ')

        resultList[:] = [] # empty the list
        if count == 4:
            print("You guessed right! It took " + str(guesses) + " guesses.\n")
            break

    #if again = "quit":
        #playAgain = 0
    # ------ inner loop end

CowsAndBulls()

# ask the user the strength of the password to be generated
from collections import namedtuple
import random

class NumberStruct:
    count = 0
    #recent = 0
    low = 48
    high = 57

    # dont really need getters and setters
    #def getCount():

class UpperLettersStruct:

    # The class "constructor" - It's actually an initializer
    #def __init__(self, name, age, major):

    count = 0
    #recent = 0
    low = 65
    high = 90

class LowerLettersStruct:
    count = 0
    #recent = 0
    low = 97
    high = 122

class SymbolsStruct:
    count = 0
    #recent = 0
    low = 33
    high = 47

def PasswordGenerator(strength):

    userIN = strength.lower()

    numRange = UpperLettersStruct()
    l_letRange = LowerLettersStruct()
    u_letRange = UpperLettersStruct()
    symRange = SymbolsStruct()

    rangesList = [numRange, l_letRange, u_letRange, symRange]

    #weak range is 33 to 122

    #ascii
    # number range in decimal
    #dec_numbers = namedtuple("numbers", count = 0, recent = 0, low = 48, high = 57)
    #num_Low = 48
    #num_High = 57

    #uppercase letters
    #uppLet_Low = 65
    #uppLet_High = 90

    #lowercase letters
    #lowLet_Low = 97
    #lowLet_High = 122

    # some symbols
    #sym_Low = 33
    #sym_high = 47

    password = ""

    if(userIN == "weak"):
        # weak password with minimum 5 characters and max generated of 10
        # random characters chosen with no guarentee of mix containing all; numbers, letters, and symbols.
        for x in range(random.randint(5,10)):
            #convert to ascii char from int
            password += str(chr(random.randint(33,122)))
    elif (userIN == "strong"):
        # random up to 10 char
        for y in range(10):
            chosen = random.randint(33,122)
            password += chr(chosen)

            for elem in rangesList:
                if(elem.low <= chosen <= elem.high):
                    elem.count += 1
                    break

        # after random, fill in missing
        for elem in rangesList:
            if(elem.count == 0):
                password += chr(random.randint(elem.low, elem.high))

        for z in range (len(password), random.randint(15, 20)):
            password += chr(random.randint(33, 122))


    else:
        print ("invalid input")

    return password


#main
if __name__== "__main__":
    s_gen = PasswordGenerator(input("What strength would you like the password to be? (weak/strong) "))

    print (s_gen)

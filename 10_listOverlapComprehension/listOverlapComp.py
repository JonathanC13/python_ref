# with two random lists, may be different sizes, use list comprehensions to determine overlap (without duplicates)

import random

def ListOverlapComp():

    aList_size = random.randint(5, 25)
    bList_size = random.randint(5, 25)

    aList = random.sample(range(25), aList_size)
    bList = random.sample(range(25), bList_size)
    result = []

    result = [elemA for elemA in aList if elemA in bList if elemA not in result]

    print("List 1: ")
    print(*aList, sep=', ')
    print ("\n")

    print ("List 2: ")
    print(*bList, sep=', ')
    print("\n")

    print("Result: ")
    print(*result, sep=', ')
    print ("\n")

    # for elemA in aList:
        # if elemA in bList

                # store if not duplicate
                # if elemA not in result

                    # result.append(elemA)

ListOverlapComp()

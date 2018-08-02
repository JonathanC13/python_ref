# with randomly generated lists, determine which values appear in both. New list should have no duplicates

import random

def ListOverlap():

    list_size1 = random.randint(5, 10)
    list_size2 = random.randint(5, 10)

    # dynamic arrays
    list1 = []
    list2 = []
    resultList = []

    #for x in range(2, 30, 3): start, end, incre
    for x in range(list_size1):
        randValue = random.randint(0, 10)
        list1.append(randValue)

    for y in range(list_size2):
        randValue = random.randint(0, 10)
        list2.append(randValue)

    for z in range(len(list1)):
        # check for overlap
        if list1[z] in list2:

            if list1[z] in resultList:
                #do nothing
                pass
            else:
                resultList.append(list1[z])



    print("List 1 contains: ")
    print (*list1, sep=', ')
    print ("\n")

    print("List 2 contains: ")
    print (*list2, sep=', ')
    print ("\n")

    print ("The result List is: ")
    print (*resultList, sep=', ')

ListOverlap()

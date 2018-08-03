# using sets have a list that has no duplicates

# sets are an unordered list of unique values, can do list functions except indexing

def sets_noDup(userList = "Input the list you would like to be put through a set (seperated by a space): "):

    userIn = [int(x) for x in input(userList).split()]

    result = set(userIn) #convert to set, removes duplicates

    print(result)



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
        randValue = random.randint(0, 5)
        list1.append(randValue)

    for y in range(list_size2):
        randValue = random.randint(0, 5)
        list2.append(randValue)

    for z in range(len(list1)):
        # check for overlap
        if list1[z] in list2:

            resultList.append(list1[z])

    # deal with duplicates by converting it into a set
    finalList = set(resultList)

    print("List 1 contains: ")
    print (*list1, sep=', ')
    print ("\n")

    print("List 2 contains: ")
    print (*list2, sep=', ')
    print ("\n")

    print ("The result List is: ")
    print (finalList)
    print("\n")

    print("Turning set back to list, check if worked by getting an index[0]: ")
    listlist = list(finalList)
    print(listlist[0])


#sets_noDup()
ListOverlap()

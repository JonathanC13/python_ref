# Takes an user number and checks the list for values less than it.

def LessThanTen():

    aList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lesserList = []

    lessValue = int(input("State the number that will be compared to the list: "))

    i = 0
    for element in aList:
        if (aList[i] < lessValue):
            lesserList.append(aList[i])
        i += 1

    # after filling the second array just print
    print("The new list is: ")
    print (*lesserList, sep = "," )

LessThanTen()

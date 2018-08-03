# Takes an user number and checks the list for values less than it.

def LessThanTen():

    aList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lesserList = []

    lessValue = int(input("State the number that will be compared to the list: "))

    
    for element in aList:
        if (element < lessValue):
            lesserList.append(element)
        

    # after filling the second array just print
    print("The new list is: ")
    print (*lesserList, sep = "," )

LessThanTen()

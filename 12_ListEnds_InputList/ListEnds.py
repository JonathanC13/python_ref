# takes a list then creates a list with only the first and last element

def ListEnds():

    print("Input a list of values, seperated by a space: ")
    userList = [int(x) for x in input().split()]

    result = []

    #check if list empty
    if not userList:
        print ("List is empty")

    else:
        result.append(userList[0])
        x = userList.pop()
        result.append(x)

    print("Result is: ")
    print(*result, sep=', ')
    print("\n")

ListEnds()

# With the user input value, determine all its divisors

def Divisors():

    inputVal = int(input("What number would you like to know the divisors for? "))

    x = range(2, inputVal)
    divList = []

    i = 0
    for element in x:
        if ((inputVal % x[i]) == 0):
            divList.append(x[i])

        i += 1

    # end print the results
    print("The divisors for " + str(inputVal) + " are ")
    #print str(divList)[1:-1] # :-1 means the last element
    print (*divList, sep=', ')

Divisors()

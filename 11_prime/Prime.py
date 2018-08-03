# Determine if the user input value is prime or not



def Divisors(help_text = "What number would you like to check if it is prime? "):

    inputVal = int(input(help_text)) # argument input

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

    return divList

def Prime():

    userIn = Divisors() # returns a List if the divisors

    if (len(userIn) == 0):
        print("This number is prime!")
    else:
        print ("This number is not prime!")


# call
Prime()

# Get the max value from 3 user inputs without using the max() function

def maxOfThree(help_text = "Input 3 values:"):
    #inputArray = input(help_text); #default split at space

    inputArray = [int(x) for x in input(help_text).split()] # ensure split by space

    a = inputArray[0]
    b = inputArray[1]
    c = inputArray[2]

    max = 0

    # a equal or greater than b
    if(a >= b) and (a >= c):
        max = a
    elif(b >= a) and (b >= c):
        max = b
    elif(c >= a) and (c >= b):
        max = c

    print("The max value is " + str(max));

    return max

a = maxOfThree()
print("yeet " + str(a))

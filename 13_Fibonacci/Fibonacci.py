# ask the user how many Fibonacci numbers they would like to be printed

def FibonacciGen (number_of = "How many Fibonacci numbers would you like to be generated? "):

    x = int(input(number_of))

    fibList = []

    # need to fill the first 2 positions
    if x >= 0:
        fibList.append(0)
    if x >= 1:  # in fib the first value is 1 not 0
        fibList.append(1)

    # if more than 2 means we can execute the algorithm
    if x >= 2:
        for x in range(2, x):
            fibList.append(fibList[x-2] + fibList[x-1])

    print("The result list is: ")
    print(*fibList, sep=', ')
    print("\n")

FibonacciGen()

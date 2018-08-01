# takes a user number and determines if it is Odd or even

def OddOrEven():

    while True:
        num = input("What number would you like to check if it is odd or even? (Type 'exit' to exit) ")

        if (num == "exit"):
            break;

        num = int(num)
        mod4 = num % 4
        mod2 = num % 2 # remainder

        if mod4 == 0:
            print ("This number is a mutiple of 4.")

        if mod2 == 1:
            print ("This number is odd.")
        else:
            print ("This number is even.")

    print ("Thank you, closing.")

    
OddOrEven()

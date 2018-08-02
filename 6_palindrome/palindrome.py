# user input string, check if it is a palindrome (spelled the same backwards as forward)

def Palindrome():

    userIn = input("What string would you like to check that is a palindrome? ")

    i_len = len(userIn)

    #check if odd or even letters
    modLetters = i_len % 2
    flag_palin = 1  # 1 for true

    if (modLetters == 0):
        for x in range (int(i_len/2)): #end at (i_len/2) -1
            # check letters
            if userIn[x] != userIn[i_len - x -1]:
                flag_palin = 0
                break
    else:
         for x in range (int(i_len//2)): #floor division
             # check letters
             print("checking: " + userIn[x] + " and " + userIn[i_len - x -1])
             if userIn[x] != userIn[i_len - x-1]:
                 flag_palin = 0
                 break

    if (flag_palin == 1):
        print ("This word is a palindrome")
    else:
        print ("This word is not a palindrome")

Palindrome()

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

    print("second method of checking with no length division");
    i = 0; #starting index
    j = i_len-1;  #end length
    pal_flag = 0;

    if(j == 0):
        print("input string is empty");
    else:
        while(i < j):
            if (userIn[i] != userIn[j]):
                pal_flag = 11;
                break
            i = i + 1;
            j = j - 1;
        # user message
        if (pal_flag == 0):
            print(userIn + " is a palindrome");
        else:
            print(userIn + " is not a palindrome");

Palindrome()

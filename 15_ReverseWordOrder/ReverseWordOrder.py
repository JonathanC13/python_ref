# with the user input, reverse the word order.

def ReverseWordOrder(text):

    userIn = input(text)

    # split on whitespace
    wordList = userIn.split()

    #can just make a resultlist to place the reverse word

    # range(0, 6) is 0 to 5
    for x in range(len(wordList) // 2): # floor divide
        temp = wordList[len(wordList) - x - 1]
        wordList[len(wordList) - x - 1] = wordList[x]
        wordList[x] = temp

        # split by space.join
    # result = " ".join([word for word in wordList[::-1]])

    print (wordList)

ReverseWordOrder("What sentence would you like to reverse? ")

# with the user input, reverse the word order.

def RevereWordOrder(text):

    userIn = input(text)

    # split on whitespace
    wordList = userIn.split()

    # range(0, 6) is 0 to 5
    for x in range(len(wordList) // 2): # floor divide
        temp = wordList[len(wordList) - x - 1]
        wordList[len(wordList) - x - 1] = wordList[x]
        wordList[x] = temp

    print (wordList)

RevereWordOrder("What sentence would you like to reverse? ")

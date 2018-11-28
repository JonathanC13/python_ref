
# range for letters in decimal
class ASCII_dec_letters:
    min_range = 0
    max_range = 0
    def set_range(self, min, max):
        self.min_range = min;
        self.max_range = max;

class letterGuesser:
    def guessLetters(self, chosenWord):

        low_letterRange = ASCII_dec_letters();
        low_letterRange.set_range(97, 122);

        up_letterRange = ASCII_dec_letters();
        up_letterRange.set_range(65, 90);

        #rangeList = [low_letterRange, up_letterRange]

        chosen = chosenWord.lower()
        print("Word is " + chosen)
        chosenLength = len(chosenWord)
        solvedWord = ['_'] * chosenLength
        guessedLetters = []

        solved_flag = 11; # flag if the word has been completed
        guessCount = 0;

        print("Hang man game.\n")
        # game process
        while(solved_flag == 11):
            print("\n------\n")
            print(*solvedWord, sep=', ')
            print("Guess count " + str(guessCount))

            # check if game over
            if '_' not in solvedWord:
                print("Word solved.")
                break;

            if(guessCount >= 6):
                print("Out of guesses!")
                break;

            inputLetter = input("Please input a letter you would like to guess: \n")

            # check if valid input
            # test length
            if(len(inputLetter) > 1) or (len(inputLetter) < 1):
                print("Invalid input: Need only 1 letter input.\n")
                continue;
            else:
            # if length of 1, check if it is a letter. use Ascii
                if(up_letterRange.min_range < ord(inputLetter) < up_letterRange.max_range):
                    # if upper, convert to lower to be conform
                    inLet = inputLetter.lower();
                elif(low_letterRange.min_range > ord(inputLetter)) or (low_letterRange.max_range < ord(inputLetter)):
                    # not a lower case letter
                    print("Invalid input: Not a letter. \n")
                    continue
                else:
                    inLet = inputLetter

                # check if this letter was guessed before
                if inLet in guessedLetters:
                    print("Letter was guessed before. \n")
                    continue

            # valid input, so we can continue the game process
            # add to guessedLetters
            print("With guess: " + inLet)
            guessedLetters.append(inLet)

            print("Guessed letters: ")
            print(*guessedLetters, sep=', ')

            found = 11;
            # check if the guessed letter is in the chosen word
            for x in range(0, chosenLength):
                # if match, place in solved word
                if(inLet == chosen[x]):
                    found = 0
                    solvedWord[x] = inLet

            # not found in word, so guess count increases
            if(found == 11):
                guessCount += 1;
                self.drawHangman(guessCount)

    def drawHangman(self, count):
        head =  ' o'
        l_arm = '/'
        r_arm = '\\'
        body =  '|'
        l_leg = '/'
        r_leg = ' \\'

        # adding parts 1 by 1
        if (count >= 1):
            print(head)
        if(count >= 2):
            print(l_arm, end='')
        if(count >= 3):
            print(body, end='')
        if(count >= 4):
            print(r_arm)
        if(count >= 5):
            print(l_leg, end='')
        if(count == 6):
            print(r_leg)


#guessLetters('YEET')

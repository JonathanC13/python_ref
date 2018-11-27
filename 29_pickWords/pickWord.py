import random

def pickWord():

    #open file
    with open('dict.txt', 'r') as open_file:
        #set list as contents of file
        words = list(open_file)

        #need to pick a random word from the list, strip spaces
        return random.choice(words).strip()

        # alternative is:
        # fill words list with each line from the txt file
        # pick random element from 0 to len(words)

chosenWord = pickWord();
print("The chosen word is " + chosenWord);

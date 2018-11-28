from guessLetters import *
from pickWord import *

class HangmanGame:

    def gameProcess(self):

        # pick the word
        o_wordPick = wordPicker()
        s_pickedW = o_wordPick.pickWord()

        # initiate guesser
        o_letterGuess = letterGuesser()
        o_letterGuess.guessLetters(s_pickedW)


hang = HangmanGame()
hang.gameProcess()

# 1. Initialize the board and list that holds the values
# 2. Get the user move, check if it is valid
# 3. If valid and enough moves have been made, check win conditions.


# import item, class DrawBoard
from DrawBoard import DrawBoard
from TTTwinSETS import *

class TTT():

    # constructor ==============================================================
    def __init__(self):
        self.boardSize = 3
        self.player = "X"
        # initialize board values
        self.Matrix = [["__" for x in range(boardSize)] for y in range(boardSize)]

    def changePlayer(self):
        if self.player == "X":
            self.player = "O"

        else:
            self.player = "X"


    def checkValid_update(self, move):
        valid = 1

        x = move[0]
        y = move[1]

        if (x >= 0) and (x <= 3) and (y >= 0) and (y <= 3):
            if (self.Matrix[x][y].strip() != "X") and (self.Matrix[x][y].strip() != "O"):
                self.Matrix[x][y] = self.player +" "
            else:
                valid = 0
        else:
            valid = 0

        return valid


    def gameProcess(self):

        print("Tic Tac Toe")
        #Draw the board
        printBoard = DrawBoard()
        printBoard.drawGameState(self.boardSize, self.Matrix)

        turnCount = 0
        playerNum = 1

        again = 1

        while again == 1:

            while True:

                print("Player " + self.player + " turn - options (1 2 3 quit) in format '1, 2': ")
                userIn = input()

                if (userIn == "quit"):
                    again = 0
                    break



                # need to take care of indexing and spaces
                moveList = userIn.split(",")
                moveList[0] = moveList[0].strip()
                try:
                    moveList[0] = int(moveList[0]) - 1
                except ValueError:
                    print("Not an integer.")
                    continue

                moveList[1] = moveList[1].strip()
                try:
                    moveList[1] = int(moveList[1]) - 1
                except ValueError:
                    print("Not an integer.")
                    continue

                # check if valid move ==========================================
                if self.checkValid_update(moveList) == 0:
                    print("Invalid input, Try again.")
                    continue

                turnCount += 1
                p_move = Move(moveList[0], moveList[1])

                print(self.Matrix)

                # print the current state of the game ==========================
                printBoard.drawGameState(self.boardSize, self.Matrix)

                # if there has been more than 5 turns, then start checking win conditions
                if (turnCount > 4):

                    if (checkHorAndVert(self, p_move) == 1) or checkDiagonals(self, p_move):
                        print("Player " + str(self.player) + " has won!")
                        break
                    # else keep playing
                # change player
                self.changePlayer()

            userAgain = input("Would you like to play again? (y/n) ")
            if (userAgain == "n"):
                break


class Move():

    def __init__(self, i_x, i_y):
        self.x = int(i_x)
        self.y = int(i_y)

    def getMoveX(self):
        return self.x

    def getMoveY(self):
        return self.y


playTTT = TTT()
playTTT.gameProcess()

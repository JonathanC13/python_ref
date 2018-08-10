# functions to test win conditions for tictactoe
# a cool solution was using sets then checking the length. If len 1 means all positions had the same value meaning win!

boardSize = 3

# Checks the horizontal plane if the move is a winning one
# input: TTT is the game instance, The Y position of the move object
# output: Boolean of won or not
def checkHorizontal(TTT, moveY):

    row = move.getY()

    won_flag = 1
    for col in range(TTT.boardSize):
        if(TTT.board[col][row] != TTT.player):  # list y, items of 0 1 2
            won_flag = 0
            break

    return won_flag

def checkVertical(TTT, moveX):

    col = move.getX()

    won_flag = 1

    for row in range(TTT.boardSize):
        if (TTT.board[row][col] != TTT.player): #lists 0 1 2, get item x
            won_flag = 0
            break

    return won_flag

def checkDiagonals(TTT):


    won_flag = 1

    # NW to SE
    for a in range(TTT.boardSize):
        if(TTT.board[a][a] != TTT.player):
            won_flag = 0
            break

    if won_flag != 1:
        # SW to NE
        i = 0
        for c in range(TTT.boardSize -1):
            if (TTT.boardSize[c][i] != TTT.player):     #list, item
                won_flag = 0
                break
            else:
                won_flag = 1

            i += 1



    return won_flag

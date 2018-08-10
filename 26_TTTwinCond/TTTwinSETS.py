# using sets to determine if the player has won
boardSize = 3

# Check the horizontal and vertical plane if player has won with their move
# Input: instance of the TTT game, current move
# Output: int: flag if won or not
def checkHorAndVert(TTT, move):

    won_flag = 1
    m_row = move.getY()
    m_col = move.getX()

    rowSet = set()  #empty set
    colSet = set()

    # checking horizontal
    for col in range(TTT.boardSize):
        rowSet.add(TTT.board[m_row][col])     # list, item

    # checking vertical
    for row in range(TTT.boardSize):
        colSet.add(TTT.board[row][m_col])

    # if none are length 1, meaning no duplicates then they have not won with this move
    if (len(rowSet) != 1 and len(colSet) != 1):
        won_flag = 0

    return won_flag

def checkDiagonals(TTT, move):

    #check if move was a corner or middle, if not no need to check. Maybe do this in main

    forSet = set()
    backSet = set()

    # check diagonals
    # NW to SE
    for pos in range(TTT.boardSize):
        forSet.add(TTT.board[pos][pos])

    i = 0
    for list in range(TTT.boardSize -1, -1, -1):
        backSet.add(TTT.board[list][i])
        i += 1

    if (len(forSet) != 1 and len(backSet) != 1):
        won_flag = 0

    return won_flag

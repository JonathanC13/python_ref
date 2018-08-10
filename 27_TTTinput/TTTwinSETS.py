# using sets to determine if the player has won
boardSize = 3

# Check the horizontal and vertical plane if player has won with their move
# Input: instance of the TTT game, current move
# Output: int: flag if won or not
def checkHorAndVert(TTT, move):

    won_flag = 1
    m_row = move.getMoveY()
    m_col = move.getMoveX()

    rowSet = set()  #empty set
    colSet = set()

    # checking horizontal
    for col in range(TTT.boardSize):
        rowSet.add(TTT.Matrix[m_row][col])     # list, item

    # checking vertical
    for row in range(TTT.boardSize):
        colSet.add(TTT.Matrix[row][m_col])

    # if none are length 1, meaning no duplicates then they have not won with this move
    if (len(rowSet) != 1 and len(colSet) != 1):
        won_flag = 0

    return won_flag

def checkDiagonals(TTT, move):

    invalid = [(0,1),(1,0),(1,2), (2,1)]

    #check if move was a corner or middle, if not no need to check.
    q = move.getMoveX()
    w = move.getMoveY()

    if (q == 0 and w == 1) or (q == 1 and (w == 0 or w == 2)) or (q == 2 and w == 1):
        return 0

    won_flag = 1
    forSet = set()
    backSet = set()

    # check diagonals
    # NW to SE
    for pos in range(TTT.boardSize):
        forSet.add(TTT.Matrix[pos][pos])

    i = 0
    for list in range(TTT.boardSize -1, -1, -1):
        backSet.add(TTT.Matrix[list][i])
        i += 1

    if (len(forSet) != 1 and len(backSet) != 1):
        won_flag = 0

    return won_flag

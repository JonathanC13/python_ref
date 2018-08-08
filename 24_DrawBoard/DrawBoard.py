# ask the user for size of board then draw it accurately

class DrawBoard():

    def drawRowLine(self, num_lines):
        s_lines1 = ""
        for x in range(num_lines):
            s_lines1 += " ---"

        return s_lines1

    def drawColLine(self, num_lines):
        s_lines2 = ""

        for y in range(num_lines+1):
            s_lines2 += "|   "

        return s_lines2

if __name__ == "__main__":
    userIn = int(input("What size symmetic grid would you like? (3 for 3x3) "))

    board = DrawBoard()
    hor = board.drawRowLine(userIn)
    vert = board.drawColLine(userIn)

    # for the row
    for x in range(userIn):
        #for the col
        print(str(hor))
        print(str(vert))



    # for the bottom of the last row, add the row lines
    print(str(hor))

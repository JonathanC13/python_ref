# ask the user for size of board then draw it accurately

class DrawBoard():

    def drawRowLine(self, num_lines):
        s_lines1 = ""
        for x in range(num_lines):
            s_lines1 += "-----"

        return s_lines1

    def drawColLine(self):
        s_lines2 = ""

        s_lines2 += "| "

        return s_lines2

    def drawGameState(self, boardSize, gameState):

        # board values
        Matrix = gameState

        hor = self.drawRowLine(boardSize)


        for list in range(boardSize):
            # for the row
            print(str(hor))

            # item
            for y in range(boardSize):
                print(self.drawColLine(), end ="")

                print(Matrix[list][y], end="")
                print(" ", end="")


            print(self.drawColLine())



        # for the bottom of the last row, add the row lines
        print(str(hor))

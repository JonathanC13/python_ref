# rock paper scissors game

def RockPaperScissors():

    while True:

        in_p1 = input("P1: Rock, paper, or Scissors? ")
        in_p2 = input("P2: Rock, paper, or Scissors? ")

        p1 = in_p1.lower()
        p2 = in_p2.lower()

        r = "rock"
        p = "paper"
        s = "scissors"

        if (p1 == r):
            if(p2 == p):
                print("Player 2 wins!")
            elif (p2 == r):
                print("Tie!")
            else:
                print("Player 1 wins!")

        elif (p1 == p):
            if(p2 == s):
                print("Player 2 wins!")
            elif (p2 == p):
                print("Tie!")
            else:
                print("Player 1 wins!")

        elif (p1 == s):
            if(p2 == r):
                print("Player 2 wins!")
            elif (p2 == s):
                print("Tie!")
            else:
                print("Player 1 wins!")

        else:
            print("Some one had an invalid input.")

        again = input("Would you like to play again? (type 'quit' to quit or anything for another round) ")

        if (again == "quit"):
            break
        else:
            continue

    print ("done.")

RockPaperScissors()

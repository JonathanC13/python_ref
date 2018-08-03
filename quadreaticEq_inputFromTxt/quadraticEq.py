
# quardratic formula has 3 variable values: a, b, and c. They are the co-efficients of x^2, x, and x^0 respectively.
# must rely on user to fill text file in correct order of a, b, and c.
# could do a console input for the values, but may be tedious for the user.

import math

class QuadraticEquationSolver:
    def quadFormulaFunction(self):


        #scan for the ordered variables in the textfile
        # text file, must escape '\'
        f = open('C:\\Users\\Jonathan\\Desktop\\test1\\quadreaticEq\\variableValues.txt','r')

        # array of values and parse with whitespace
        s_arr_varValues = (f.read()).split()

        # assign the array values to named variables
        a = int(s_arr_varValues[0])
        b = int(s_arr_varValues[1])
        c = int(s_arr_varValues[2])

        print ("a: " + str(a) + " b: " + str(b) + " c: " + str(c))

        # check if the Discriminant is negative, if yes then no real distinct roots, only imaginary
        discr = math.pow(b,2) - 4*a*c
        if(discr < 0):
            print("This quadratic equation has no real roots.")
        else:
            numerator1 = - b + math.sqrt(discr)
            numerator2 = - b - math.sqrt(discr)
            denom = 2*a

            root1 = numerator1 / denom
            root2 = numerator2 / denom

            print ("This quadratic equation has real roots of x1 = " + str(root1) + " and x2 = " + str(root2))
#run
quadEq = QuadraticEquationSolver()

quadEq.quadFormulaFunction()

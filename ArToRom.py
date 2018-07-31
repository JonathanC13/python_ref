
class Arabic_to_roman:
    def numerals(self):
        #scan for arabic numeral for console arg or textfile
        # text file, must escape '\'
        f = open('C:\\Users\\Jonathan\\Desktop\\test1\\InputValue.txt','r')

        s_ar_num = f.read()

        # string cast to int
        ar_num = int(s_ar_num)

        # empty string
        s_roman = ''

        # do conversion to roman
        while (ar_num >= 1000):
            ar_num -= 1000
            s_roman += 'M'
        while (ar_num >= 900):
            ar_num -= 900
            s_roman += 'CM'
        while (ar_num >= 500):
            ar_num -= 500
            s_roman += 'D'
        while (ar_num >= 400):
            ar_num -= 400
            s_roman += 'CD'
        while (ar_num >= 100):
            ar_num -= 100
            s_roman += 'C'
        while (ar_num >= 90):
            ar_num -= 90
            s_roman += 'XC'
        while (ar_num >= 50):
            ar_num -= 50
            s_roman += 'L'
        while (ar_num >= 40):
            ar_num -= 40
            s_roman += 'XL'
        while (ar_num >= 10):
            ar_num -= 10
            s_roman += 'X'

        while (ar_num >= 9):
            ar_num -= 9
            s_roman += 'IX'
        while (ar_num >= 5):
            ar_num -= 5
            s_roman += 'V'
        while (ar_num >= 4):
            ar_num -= 4
            s_roman += 'IV'
        while (ar_num >= 1):
            ar_num -= 1
            s_roman += 'I'

        print ("Given arabic numeral: " + str(s_ar_num) + ". The roman conversion is: " + str(s_roman) + ".")

# main run
run = Arabic_to_roman()

run.numerals()

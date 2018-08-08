# write to a txt file

from DecodeWebPage import DECODE

def WriteToFile():

    DEC = DECODE()
    retList = DEC.DecodeWebPage()

    f = open('C:\\Users\\Jonathan\\Desktop\\test1\\21_WriteToFile\\textfile.txt','w')

    for elem in retList:
        f.write(str(elem))
        f.write("\n")

    f.close()
    
WriteToFile()

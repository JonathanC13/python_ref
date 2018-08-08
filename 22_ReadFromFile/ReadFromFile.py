# read from file and count how many images belong in each category

def ReadFromFile():

    cate_dict = {}

    tempList = []

    with open('Training_01.txt', 'r') as open_file:
        line = open_file.readline()
        tempList = line.split("/")
        print(tempList)
        # while it has a next line
        while line:
            # empty the list
            tempList [:] = []

            # list containing the strings split by "/"
            tempList = line.split("/")
            category = tempList[2]  # in the text file the category is consistently in position 2. tempList = ['', a, abbey, jpg]

            # if the key already exists
            if category in cate_dict:
                cate_dict[category] += 1
            # add new key
            else:
                cate_dict[category] = 0

            #print(line)
            line = open_file.readline()   # get next line

    for pair in cate_dict.items():
        print (pair)

    open_file.close()


ReadFromFile()

# taking 2 files, find the values that overlap

def FileOverlap(fileOne, fileTwo):

    List_1 = fileOne.read().splitlines()
    List_2 = fileTwo.read().splitlines()

    result = []

    for val in List_1:
        if val in List_2:
            result.append(val)
            print(str(val))

    #print(*finalList, sep=', ')


if __name__ == "__main__":
    file_1 = open("primenumbers.txt", "r")
    file_2 = open("happynumbers.txt", "r")

    FileOverlap(file_1, file_2)

    file_1.close()
    file_2.close()

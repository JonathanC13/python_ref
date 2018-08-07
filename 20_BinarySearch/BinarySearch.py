# takes an ordered list and a user number, then it checks the list if it contains it.

# splits the list until the value is found at the pivot point
def BinarySearch(userSpec):

        #scan for the ordered list values in the textfile
        # text file, must escape '\'
        f = open('C:\\Users\\Jonathan\\Desktop\\test1\\20_BinarySearch\\orderedList.txt','r')

        # array of values and parse with whitespace
        listValues = (f.read()).split()

        userIn = str(input(userSpec))

        first = 0
        last = len(listValues) - 1
        found = 0

        while first <= last and not found:
            pivot = (first + last)//2   # floor divide
            # value found at the pivot point
            if userIn == listValues[pivot]:
                print("Value is found at index: " + str(pivot))
                found = 1
            # value is less than the pivot, so focus on that side
            elif (userIn < listValues[pivot]):
                last = pivot-1
            # value is greater than the pivot
            else:
                first = pivot + 1
        if not found:
            print("Value not in list.")

BinarySearch("What number would you like to check if it is in the list? ")

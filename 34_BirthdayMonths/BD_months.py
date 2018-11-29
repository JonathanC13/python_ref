import json
from collections import Counter

class BD_months():
    def getMonthCount(self):

        BdaysAll = []
        # open file for reading
        with open('BD_Json.json', 'r') as open_file:
            inputJson = json.load(open_file)
            #print the names
            for name in inputJson:
                print(name + " : " + inputJson.get(name));
                BdaysAll.append(inputJson.get(name))

        BdayMonth = []
        # parse the birthday months into a list
        for bday in BdaysAll:
            bdayParse = bday.split("/")
            print(bdayParse[0] + ", " + bdayParse[1] + ", " + bdayParse[2])
            BdayMonth.append(bdayParse[0])

        print(*BdayMonth, sep=', ')

        switcher = {
            "01": "Jan",
            "02": "Feb",
            "03": "Mar",
            "04": "Apr",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "Aug",
            "09": "Sept",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec"
        }

        s_monthsCount = [] #instead of a dict with set months, we'll follow the exercise and create a list, then use Counter from collections lib
        for month in BdayMonth:
            s_monthsCount.append(switcher.get(month, "invalid"))

        c = Counter(s_monthsCount)
        print(c)
        return c

BDmn = BD_months()
cc = BDmn.getMonthCount()

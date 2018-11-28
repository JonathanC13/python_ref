
class BirthdayDict:

    def chooseBday(self):

        Birthdays = {
            "Steven" : "1/1/1995",
            "Jarvis" : "2/2/1995"
        }

        print("Birthday dictionary, we have the birthdays of: ")
        for names in Birthdays:
            print(names)

        inputName = input("Who's birthday would you like to know: \n")
        # second argument of get() is the default response if not in list
        print(Birthdays.get(inputName, "Name is not in dictionary."))

        """
        # predefined dictionaries of people's birthdays
        Bday_1 = {"Name" : "Steven", "Birthday" : "1/2/1995"}
        Bday_2 = {"Name" : "Jarvis", "Birthday" : "2/3/1995"}

        # list of dictionaries
        BdayList = [Bday_1, Bday_2]

        print("Birthday Dictionary. We have the birthdays of: ")
        for x in range(0, len(BdayList)):
            # access List = dict.get["name"]
            #print(BdayList[x]["Name"])
            print(BdayList[x].get("Name"))

        inputName = input("Who's birthday would you like to know? \n")

        # second argument of get() is the default response if not in list
        #print(SomeDict.get("Name", "Name not on the list"))

        found_flag = 11;
        for dict in BdayList:
            if(inputName == dict["Name"]):
                print(dict["Birthday"])
                found_flag = 0;
                break

        if (found_flag == 11):
            print("Name not on the list.")
        """
retBday = BirthdayDict()
retBday.chooseBday()

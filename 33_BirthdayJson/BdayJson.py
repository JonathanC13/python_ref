import json

# info_about_me = {
#    "name": "Michele",
#    "has_a_dog": False
#}
# save to file
# json.dump(info_about_me, f)


class BdayJson:
    def AccessJson(self):

        # display current json names to user
        print("Birthday JSON, the birthdays that are available are: ")
        # open file
        # r+, read and write. Stream position at start of file
        with open('BD_Json.json', 'r+') as open_file:
            inputJson = json.load(open_file)
            #print the names
            for name in inputJson:
                print(name)

            # ask user if they want to get a birthday or add one
            inputOption = input("Would you like to (add) or (get) a birthday: (for 'get' can use >> get name) >> ").split()

            if(inputOption[0] == 'add'):
                inputAdd = input("Add a person and their birthday in the format >> Todd 1/3/2000 >>").split()
                # add to json and dump into file?
                if(len(inputAdd) == 2):
                    if inputAdd[0] in inputJson:
                        inputConfirm = input("Name already exists in file, would you like to overwrite (Y/N): ").lower()
                        if(inputConfirm == "n"):
                            pass
                        else:
                            #inputJson.update({inputAdd[0] : inputAdd[1]})
                            inputJson[inputAdd[0]] = inputAdd[1]
                            open_file.seek(0) # reset file position to beginning
                            json.dump(inputJson, open_file)
                            open_file.truncate()
                else:
                    print("Not enough information provided.")
            elif (inputOption[0] == 'get'):
                if(len(inputOption) == 2):
                    print(inputJson.get(inputOption[1], "That name does not exist in the file."))
                elif(len(inputOption) == 1):
                    inputName = input("Enter who's birthday you would like: ")
                    print(inputJson.get(inputName, "That person does not exist in this file."))
                else:
                    print("Invalid option.")

            else:
                print("Not a valid option.")

acc_json = BdayJson()
acc_json.AccessJson()

# get user's name and age, then tells them what year they will turn 100 years old
import datetime
def characterIn():

    # get current datetime
    now_time = datetime.datetime.now()

    # scan for name
    name = input("What is your name? ")

    age = input("What is you age? ")

    repeat = int(input("How many times would you like the repeated message? "))

    # calc when they will be 100 years old
    age100 = 100 - int(age)
    year100 = now_time.year + age100



    print(repeat * ("Hello " + str(name) + ", you will be 100 years old during the year " + str(year100) + ".\n"))


characterIn()

import datetime


def year(age):
    now = datetime.datetime.now()
    year = now.year - age + 100
    return year


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name + ", you will 100 years old in the " + str(year(age)))

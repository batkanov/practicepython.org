def checkpasss(password):
    symbolsList = []
    upperCheck = False
    lowerCheck = False
    digitCheck = False
    if (len(password) < 10):
        return False
    else:
        for i in range(0, len(password)):
            symbolsList.append(password[i])

        for i in range(0, len(password)):
            if symbolsList[i].isupper():
                upperCheck = True
                break
        for i in range(0, len(password)):
            if symbolsList[i].islower():
                lowerCheck = True
                break

        for i in range(0, len(password)):
            if symbolsList[i].isdigit():
                digitCheck = True
                break

        if upperCheck and digitCheck and lowerCheck:
            return True
        else:
            return False


password = input("Enter the password: ")
print(checkpasss(password))

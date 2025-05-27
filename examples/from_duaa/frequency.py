def frequency(theList, elementCount):
    count = 0
    for item in theList:
        if item == elementCount:
            count += 1
    return count

userInput = input("What do you want to enter in the list?pls use (,) to separat the items  " )
userList = [item.strip() for item in userInput.split(",")]
element = input("What is the element you like to count?  ")

print("The Total of " , element , "is: ", frequency(userList,element))



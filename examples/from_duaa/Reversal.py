userInput = input("What do you want to enter in the list?pls use (,) to separat the items  " )
firstList = [item.strip() for item in userInput.split(",")]

def reverseList(itemsList):
   return itemsList[::-1]

print("Your List is : ", firstList)
print("The Reversed List of Your list is : ", reverseList(firstList))
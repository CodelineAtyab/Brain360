userInput = input("What do you want to enter in the list?pls use (,) to separat the items  " )
firstList = [item for item in userInput.split(",")]
allData = [65,True,"Hi",7.5]

def reverseList(itemsList):
   return itemsList[::-1]

print("Your List is : ", firstList)
print("The Reversed List of Your list is : ", reverseList(firstList))

print("The original list of all data Types :" , allData)
print("The Reversed List of all data typs",reverseList(allData))
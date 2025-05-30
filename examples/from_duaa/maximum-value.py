nums = input("Enter your list of numbers (separated by ,) OR press (Enter) for an empty list: ")
def maxForList(MaxNum):
    MaxNum.sort()
    MaxofList = MaxNum[-1]
    return MaxofList
  
if nums =="":
    listOfNumbers = []
    print("None")
else:
 listOfNumbers = [float(num) for num in nums.split(",")]
 print("The Maximum Number Of Your Code is : ", maxForList(listOfNumbers))
         
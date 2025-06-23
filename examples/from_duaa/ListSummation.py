nums = input("Enter your list of numbers (separated by ,) OR press (Enter) for an empty list: ")
if nums =="":
    listOfNumbers = []
else:
 listOfNumbers = [float(num) for num in nums.split(",")]

def sumForList(NumbersToSum):
    total = 0 
    for num in NumbersToSum:
        total += num 
    return total
print("The Sum of your List of numbers is : ", sumForList(listOfNumbers))
        

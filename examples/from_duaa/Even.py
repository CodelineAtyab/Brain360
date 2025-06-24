nums = input("Enter your list of numbers (separated by ,) :")
listOfNumbers = [int(num) for num in nums.split(",")]
def evenFilter(numsEven):
    numEven = []
    for x in numsEven:
     if x %2 == 0:
      numEven.append(x)
    return numEven
print("Your list of Even Numbers is :  ", evenFilter(listOfNumbers))


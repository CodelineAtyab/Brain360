sumation_list =[]
numbers = float(input("inter the number: "))
while numbers != 0 :
 sumation_list.append(numbers)
 numbers = float(input("inter the number: "))
print(sumation_list)
def total():
 return sum(sumation_list)
print("the total is: ", total())
    
 

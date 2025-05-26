import math
#decleration
numbers = []

#input
while True:
 user_input = (input("write down numbers to sum them (type 'sum' to stop and sum): "))
 if user_input == 'sum':
  break
 number = int(user_input)
 numbers.append(number)
 #number = int(user_input)
 #user_input.append(number)

 #process input
resault = sum(numbers)

#print
print(resault)
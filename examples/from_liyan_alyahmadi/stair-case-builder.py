#declaration
number = 0
tag = "#"

#Input
user_input = int(input("write down a nuber to build a staircase: "))

#processing Input 
for i in range(1, user_input+1):
    print(' ' * (user_input-i) + tag * i) 


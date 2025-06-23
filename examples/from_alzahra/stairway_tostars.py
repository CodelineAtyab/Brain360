num_of_star= int(input("Enter a number (the number should be ve+)"))

for i in range (1, num_of_star+1): #generate a sequance of numbers starting from 1 to num_of_star 
    if num_of_star<0:
        print("the number should be positive")
    else:
        print("*"*i)
num_of_star = int(input("Enter a number (the number should be ve+): "))

for i in range (1, num_of_star+1):  
    for j in range (1,i+1) : 
        if num_of_star<0:
            print("the number should be positive")
        else:
            print(j, end="")
    print()
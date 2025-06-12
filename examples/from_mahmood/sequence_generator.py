row = int(input("Enter the number of roes you want to print: "))
for count in range(1,row + 1):
    for i in range(1 , count+ 1):
        print(i ,end="")
    for i in range (count -1 ,0, -1) :
        print(i , end="") 
    print("")
    

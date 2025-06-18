#Declaration
Rows=int(input("enter the number of rows in the pyramid: "))

#Process
for i in range (Rows):
    for j in range( Rows - i -1):
        print(" " ,end="")

    for x in range (2 * i + 1):
        print("*" ,end="")
#Output 
    print()


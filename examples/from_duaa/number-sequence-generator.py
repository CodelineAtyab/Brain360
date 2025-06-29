try:
    numRows = int(input("Enter the number: "))
    numRows = abs(numRows)
except ValueError:
    print("Error NOT valid integer")
    exit()
for num in range(1,numRows +1) :
    for num2 in range(1,num +1) :
     print(num2, end= "")
    for num2 in range(num - 1 , 0 , -1) :
       print(num2, end= "")
    print()
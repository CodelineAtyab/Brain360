numRows = int(input("Enter the number:"))
numRows = abs(numRows)
for num in range(1,numRows +1) :
    x = numRows - num
    print(" " * x + "#" * num)
#Numeric staircase generator
rows=int(input("Enter the number of rows = "))
for row in range(1, rows + 1):
    for number in range(1, row + 1):
        print(number, end ="  ")
    for number in range(row - 1, 0, -1):
        print(number, end="  ")
    print("  ")
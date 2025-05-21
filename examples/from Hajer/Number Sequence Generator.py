rows=int(input("Enter the number of rwos = "))

for row in range(1, rows + 1):

    for num in range(1, row + 1):

        print(num, end="")

    for num in range(row - 1, 0, -1):

        print(num, end="")

    print("")
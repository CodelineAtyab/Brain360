
inputted_number = int(input("Enter the Numbers of rows: ")) # this will tell how many numbers of rows

if inputted_number > 0:
    for i in range(1, inputted_number + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print("")
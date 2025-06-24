num_of_rows=int(input("Enter the number of rows : "))


if num_of_rows <= 0:
    print("Enter a positive number greater than 0")
else:
    for i in range(1, num_of_rows + 1):
        
        for j in range(1, i + 1):
            print(j, end='')
        
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()  
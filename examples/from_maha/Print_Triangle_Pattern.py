num_of_row = int(input("Enter the number of rows"))

if num_of_row > 0:
    for x in range(1, num_of_row+1):
        print("*"*x)
    else:
        print("Enter a number more than 0")
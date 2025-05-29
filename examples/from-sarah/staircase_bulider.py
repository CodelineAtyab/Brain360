
num_of_rows = int(input("Enter number of rows: "))

if num_of_rows > 0:                   #checks if the number is positive.
    for i in range(1, num_of_rows + 1):
        print(' ' * (num_of_rows - i) + '#' * i)
else:
    print("Please enter a positive number.")
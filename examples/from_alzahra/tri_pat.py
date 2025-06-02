'''The script takes num_of_rows as an input from the user.
The output displays a triangle pattern with the specified number of rows.
Each row contains a sequence of numbers starting from 1 up to the row number.'''

num_of_rows=int(input("Enter the number of rows : "))
for i in range (num_of_rows):
    for in_count in range (i+1):
        print("1",end="")
    print("")
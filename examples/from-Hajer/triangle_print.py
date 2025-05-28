#Print triangular pattern

num_of_rows =int(input("Enter the number of rows:"))
for count in range (num_of_rows):
    for inner_count in range(count+1):
        print("*",end=" ")
    print("")  
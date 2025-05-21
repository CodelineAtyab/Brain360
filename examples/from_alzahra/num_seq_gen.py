num_of_rows=int(input("Enter the number of rows : "))

    
if num_of_rows <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    for i in range(1, num_of_rows + 1):
        # Increasing sequence: 1 to i
        for j in range(1, i + 1):
            print(j, end='')
        # Decreasing sequence: i-1 to 1
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print()  # Move to the next line
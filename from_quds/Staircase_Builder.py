num_of_rows = int(input("Enter the number of rows: ")) # Asking the user to enter the number of rows
for i in range(1, num_of_rows + 1 ):   
    print(" " * (num_of_rows - i) + "#" * i)
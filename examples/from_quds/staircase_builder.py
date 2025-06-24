num_of_rows = int(input("Enter the number of rows: ")) 
if num_of_rows > 0:
    for i in range(1, num_of_rows + 1 ):   
        print(" " * (num_of_rows - i) + "#" * i)
else:
    print("Invalid Input")
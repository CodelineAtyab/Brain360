# Task 1 Print Triangle Pattern
num_of_rows = int(input("Enter the number of rows: ")) 
if num_of_rows > 0:
    for count in range(num_of_rows):                      
        for inner_counr in range(count + 1):
            print("1", end="")
        print("")
else:
    print("invalid input")
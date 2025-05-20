num_of_rows = int(input("Enter the number of rows:"))

for i in range(1, num_of_rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
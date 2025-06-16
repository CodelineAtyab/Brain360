def number_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


num_rows = int(input("Enter the number of rows: "))

if num_rows > 0:
    number_triangle(num_rows)
else:
    print("Please enter a positive integer.")
def print_number_triangle(rows):
    if rows <= 0:
        print("Please enter a positive integer.")
        return

    for i in range(1, rows + 1):
        line = ""
        for num in range(1, i + 1):
            line += str(num)
        print(line)

num_rows = int(input("Enter the number of rows: "))
print_number_triangle(num_rows)
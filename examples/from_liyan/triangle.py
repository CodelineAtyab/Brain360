while True:
    rows_input = input("Enter the number of rows (positive integer): ")
    if rows_input.isdigit() and int(rows_input) > 0:
        rows = int(rows_input)
        break
    else:
        print("Please enter a valid positive integer!")

for i in range(1, rows + 1):
    print("1" * i)

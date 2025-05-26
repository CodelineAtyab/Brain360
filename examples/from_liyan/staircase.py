while True:
    rows_input = input("Enter a number: ")
    if rows_input.isdigit() and int(rows_input) > 0:
        rows = int(rows_input)
        break
    else:
        print("Please enter a valid number!")

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    hashes = "#" * i
    print(spaces + hashes)

while True:
    rows_input = input("Enter a number: ")
    if rows_input.isdigit() and int(rows_input) > 0:
        rows = int(rows_input)
        break
    else:
        print("Please enter a valid number!")

for i in range(1, rows + 1):
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

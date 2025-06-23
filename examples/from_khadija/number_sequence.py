while True:
    try:
        rows = int(input("Enter the number of rows: "))
        if rows > 0:
            break  # Exit loop if input is valid
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")

# Generate the number pattern
for i in range(1, rows + 1):
    # Print the increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    # Print the decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()  # Move to the next line
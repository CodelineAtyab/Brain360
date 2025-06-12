def print_number_pattern():
    while True:
        try:
            n = int(input("Input: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("Output: ")
    for i in range(1, n + 1):
        # Increasing numbers
        for j in range(1, i + 1):
            print(j, end='')
        print()  # Move to the next line

# Run the program
print_number_pattern()
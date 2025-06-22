num_of_rows = input("Input: ")

while not num_of_rows.isdigit() or int(num_of_rows) <= 0:
    # If input is invalid, display an error message and re-prompt
    print("Invalid input! Please enter a positive integer.")
    num_of_rows = input("input: ")

number = int(num_of_rows)
print("Output: ")
for i in range(1, number + 1):
    spaces = number - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
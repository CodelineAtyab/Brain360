num_of_rows = input("Enter the number of rows: ")

while not num_of_rows.isdigit() or int(num_of_rows) <= 0:
    # If input is invalid, display an error message and re-prompt
    print("Invalid input! Please enter a positive integer.")
    num_of_rows = input("input: ")

# Step 3: Convert the validated input into an integer
number = int(num_of_rows)
print("Output: ")
for i in range(number):
    output = "*" * number
    print(output)
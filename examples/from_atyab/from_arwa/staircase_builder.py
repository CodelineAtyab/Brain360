user_input = input("input: ")

while not user_input.isdigit() or int(user_input) <= 0:
    # If input is invalid, display an error message and re-prompt
    print("Invalid input! Please enter a positive integer.")
    user_input = input("input: ")

# Step 3: Convert the validated input into an integer
number = int(user_input)

# Step 4: Print the confirmation message using an f-string
#print(f"You entered a valid positive integer: {number}")

print("Output: ")

for i in range(1, number + 1):    
    #print("#" * i)  
    print(" " * (number - i) + "#" * i)


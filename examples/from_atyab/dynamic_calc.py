# Declaration
list_of_nums = []
user_input = ""
result = 0

# Input
while user_input != "done":
  user_input = input("Enter the number (done to exit): ")
  if user_input != "done":
    list_of_nums.append(int(user_input))

# Process
for num in list_of_nums:
  result = result + num

# Output
print(result)
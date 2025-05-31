def reverse_my_list(my_list):
    """
    This function takes a list and returns a new list with elements in reverse order.
    The original list is not modified.
    """
    return my_list[::-1]

# Input
user_list = []
while True:
    item = input("Write your list items (type 'done' to reverse the list): ")
    if item.lower() == 'done':
        break
    if item.strip():  
        user_list.append(item)

# Process input
reversed_list = reverse_my_list(user_list)

# Print results
if not user_list:
    print("Your list is empty.", user_list)
else:
    print("Reversed list:", reversed_list)
    print("Original list (unchanged):", user_list)


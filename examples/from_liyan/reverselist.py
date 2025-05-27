def reverse_my_list(my_list):
    """
    This function takes a list and returns a new list with elements in reverse order.
    The original list is not modified.
    """
    reversed_list = my_list[::-1]
    return reversed_list

# Input
user_list = []
while True:
    item = input("Write your list items (type 'done' to reverse the list): ")
    if item.lower() == 'done':
        break
    user_list.append(item)

# Process input
reversed_list = reverse_my_list(user_list)

# Print results
print("Reversed list:", reversed_list)
print("Original list (unchanged):", user_list)

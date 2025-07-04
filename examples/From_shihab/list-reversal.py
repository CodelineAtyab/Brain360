def reverse_my_list(input_list):
    return input_list[::-1]



user_list = []
while True:
    item = input("Enter items one by one. Type 'done' when you're finished:")
    if item.lower() == "done":
        break
    user_list.append(item)


reversed_list = reverse_my_list(user_list)


print("\nOriginal List:", user_list)
print("Reversed List:", reversed_list)
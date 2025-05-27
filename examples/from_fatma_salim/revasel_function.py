def reverse_my_list(original_list):
    reversed_list = []
    for i in range(len(original_list) - 1, -1, -1):
        reversed_list.append(original_list[i])
    return reversed_list

user_input = input("Enter elements separated by commas (e.g., 10,apple,True,3.14): ")


my_list = [item.strip() for item in user_input.split(',')]


reversed_result = reverse_my_list(my_list)

print("Reversed:", reversed_result)
print("Original:", my_list)
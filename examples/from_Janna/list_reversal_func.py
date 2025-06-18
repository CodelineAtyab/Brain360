def user_input():
    input_list = []
    value = input("Enter list elements separated by commas: ")
    if not value:
        return []
    parts = value.split(',')
    for item in parts:
        input_list.append(item)
    return input_list

def reverse_my_list(input_list):
    reversed_list = []
    for i in range(len(input_list) -1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list

original_list = user_input()
reversed_result = reverse_my_list(original_list)

print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_result}")

def reverse_my_list(original_list):
    reversed_list = []

    for i in range(len(original_list) - 1, -1, -1):
        reversed_list.append(original_list[i])

    return reversed_list


my_list=[10, "apple", True, 3.14]
reversed_result = reverse_my_list(my_list)

print("Reversed:", reversed_result)  # Output: [3.14, True, "apple", 10]
print("Original:", my_list) # the origanal list printed 
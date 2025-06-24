def reverse_my_list(input_list):
    return input_list[::-1]

user_input = input("Enter list elements separated by commas: ")


input_list = [item.strip() for item in user_input.split(',') if item.strip()]

print("Original List:", input_list)
print("Reversed List:", reverse_my_list(input_list)) 
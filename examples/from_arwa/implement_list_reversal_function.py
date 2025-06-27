def reverse_my_list(numbers):
    if not numbers:
        print("The list is empty")
    else:
        return numbers[::-1]


user_input = list(input("Enter numbers separated by space: ").split())
print("Original list: ",user_input)
reversed_list = reverse_my_list(user_input)
print("Reversed list: ",reversed_list)

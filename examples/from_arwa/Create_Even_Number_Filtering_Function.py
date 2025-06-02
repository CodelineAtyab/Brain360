# FUNCTION
def get_even_number(user_input):
    even_list = []
    for num in user_input:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# PROCESS
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", user_input)

# CALL FUNCTION & STORE RESULT
even_list = get_even_number(user_input)

# OUTPUT
print("Even list:", even_list)

def sum_list_elements(list_numbers):
    total = 0
    for num in list_numbers:
        total += num
    return total

user_input_of_nums = input("Enter numbers separat themby spaces: ")

list_numbers = []
for num_string in user_input_of_nums.split():
    list_numbers.append(float(num_string)) 

result = sum_list_elements(list_numbers)
print("The sum is = ", result)


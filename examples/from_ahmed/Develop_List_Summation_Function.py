
num_list =[]


def summation(o_list):
    sum_count = 0
    for num in o_list:
        sum_count = sum_count + num
    return sum_count


print("Enter a set of numbers and type 'done' once finished")
user_input = input()

if user_input == '':
    print(num_list)
else:
    while user_input != "done": 
        num_list.append(float(user_input))
        user_input = input()

print("Your list of numbers is: ")
print(num_list)
print("The sum of your list numbers is: ")
sum_value = summation(num_list)
print(sum_value)
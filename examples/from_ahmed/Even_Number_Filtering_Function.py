
num_list =[]

def even_number(original_list):
    pure_list = []
    for num in original_list:
        if num % 2 == 0:
            pure_list.append(num)
    return pure_list

print("Enter a set of even and odd numbers and type '999' once finished")
user_input = input()

if user_input == '':
    print(num_list)
else:
    while user_input != "done": 
        num_list.append(int(user_input))
        user_input = input()

print("Your list of numbers is: ")
print(num_list)
print("Your list of even numbers is: ")
evennum_list = even_number(num_list)
print(evennum_list)
print("Your list of even numbers in order: ")
for num in evennum_list:
    print(num)



num_list = []

def maximum(original_list):
    maxi_list = []
    for num in original_list:
        if num > num in original_list:
            maxi_list.append(num)
            return maxi_list
        

max_num = maximum(num_list)
print("Enter your numbers and type 'done' once finished")
user_input = int(input())

if user_input == '':
    print(None)
else:
    while user_input != "done": 
        num_list.append(int(user_input))
        user_input = input()
print("Your list is of numbers is: ")
print(num_list)
print("Your maximum number is: ")
print(max_num)
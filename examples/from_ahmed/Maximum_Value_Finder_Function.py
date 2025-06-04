

num_list = []

# def maximum(original_list):
#     maxi_list = []
#     for num in original_list:
#         if original_list[0] < original_list[1]:
#             continue
#         elif original_list[1] > original_list[0]:
#             maxi_list.append(num)
#         return maxi_list

def maximum(original_list):
    
    max_num = original_list[0]
    for num in original_list:
        if num > max_num:
            max_num = num
    return max_num

        


print("Enter your numbers and type 'done' once finished")
user_input = input()

if user_input == '':
    print(None)
else:
    while user_input != "done": 
        num_list.append(int(user_input))
        user_input = input()
print("Your list is of numbers is: ")
print(num_list)

max_num = maximum(num_list)
print("Your maximum number is: ")
print(max_num)

#Implement List Reversal Function

def reverse_my_list(input_list):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list


my_list = [10, "apple", True, 3.14]
result = reverse_my_list(my_list)

print("Reversed list:", result)    
print("Original list:", my_list)   

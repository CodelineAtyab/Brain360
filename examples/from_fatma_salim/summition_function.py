
def sum_list_elements (data_points):  # function 
    total_sum=0  
    for num in data_points : # use foor loop 
       total_sum+= num
    return total_sum 


choice = input("Enter 1 to input numbers, or 2 to use an empty list: ") 

if choice == "1":
    user_input = input("Enter numbers separated by commas: ")
    numbers = [float(x) for x in user_input.split(',')] # to spilt the numbers
    print("Sum is:", sum_list_elements(numbers))

elif choice == "2":
    empty_list = []
    print("Sum is:", sum_list_elements(empty_list))

else:
    print("Invalid choice. Please enter 1 or 2.")



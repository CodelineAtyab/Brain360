# SOLUTION 1

from ast import literal_eval

# FUNCTION
def count_element_occurrences(my_data, element_to_count):
    if element_to_count in my_data:
        freq = my_data.count(element_to_count)
        print("Output:",freq)
        return freq
    elif not my_data:
        return 0

# PROCESS
my_data = list(map(literal_eval, input(f'Enter elements separated by space (if you are entering a string, please enclose it with \033[1;31m"double quotes"\033[0m): ').split()))
print(my_data)
element_to_count = literal_eval(input("Enter element you want to count: "))

# CALL FUNCTION
count_element_occurrences(my_data,element_to_count)


# SOLUTION 2

def count_element_occurrences(input_list, element_to_count):
    count = 0
    for item in input_list:
        if item == element_to_count:
            count += 1
    return count

raw_input = input("Enter the list elements separated by spaces: ")
input_list = raw_input.split()  
element_to_count = input("Enter the element to count: ")
result = count_element_occurrences(input_list, element_to_count)
print(f"Number of occurrences of '{element_to_count}':", result)

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

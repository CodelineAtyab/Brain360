elements = []

user_input = input("Enter a list of elements (separated by commas): ")
parts = user_input.split(',')
for i in parts:
    elements.append(i) 
count_element = input("Enter the desired element to count: ")

def count_element_occurrences(input_list, element_to_count):
    count = 0
    for item in input_list:
        if item == element_to_count:
            count += 1
    return count


freq = count_element_occurrences(elements, count_element)
print(f"Your list: {elements}")
print(f"'{count_element}' occured {freq} time(s) in the list.")

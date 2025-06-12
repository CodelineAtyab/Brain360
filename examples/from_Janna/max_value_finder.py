list_of_values = []

def user_input():
    value = input("Enter a list of values (separated by commas): ")
    if not value.strip(): 
        return []
    
    parts = value.split(',')
    for i in parts:
        list_of_values.append(int(i))
    return list_of_values

def max_value(numbers):
    if not numbers:
        return None  
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max

list_of_values = user_input()
print(f"List: {list_of_values}")
max_val = max_value(list_of_values)
if max_val is not None:
    print(f"The Maximum Value is {max_val}")
else:
    print("The list is empty; no maximum value found.")
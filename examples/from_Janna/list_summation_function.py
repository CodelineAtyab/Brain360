list_of_values = []

def user_input():
    value = input("Enter a list of values (separated by commas): ")
    parts = value.split(',')
    for i in parts:
        list_of_values.append(float(i))
    return list_of_values 

def sum_value(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

user_input()

print(f"List: {list_of_values}")
print(f"The Sum is {sum_value(list_of_values)}")
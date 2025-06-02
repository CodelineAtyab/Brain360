list_of_values = []

def user_input():
    value = input("Enter a list of values (separated by commas): ")
    parts = value.split(',')
    for i in parts:
        list_of_values.append(float(i))
    return list_of_values 

def sum_value():
    return sum(list_of_values)

user_input()

print(f"List: {list_of_values}")
print(f"The Sum is {sum_value()}")
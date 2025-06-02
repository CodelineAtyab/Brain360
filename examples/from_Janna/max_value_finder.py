list_of_values = []

def user_input():
    value = input("Enter a list of scores (separated by commas): ")
    parts = value.split(',')
    for i in parts:
        list_of_values.append(int(i))
    return list_of_values 

def max_value():
    return max(list_of_values)

user_input()

print(f"List: {list_of_values}")
print(f"The Maximum Value is {max_value()}")
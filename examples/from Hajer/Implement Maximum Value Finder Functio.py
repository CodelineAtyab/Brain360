#Implement Maximum Value Finder Functio

def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]

    for number in numbers[1:]:
        if number > max_value:
            max_value=number
    return max_value

scores = [78, 92, 56, 99, 85]
temperatures = [-2, -8, -1, -5]
no_values = []

print("Max score:", find_max_value(scores))         
print("Max temperature:", find_max_value(temperatures)) 
print("Max of empty list:", find_max_value(no_values))   

# Declare the function
def find_max_value(numbers):
    if numbers == []:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Test inputs
scores = [78, 92, 56, 99, 85]
temperatures = [-2, -8, -1, -5]
no_values = []

# Print outputs
print(find_max_value(scores))       # Output: 99
print(find_max_value(temperatures)) # Output: -1
print(find_max_value(no_values))    # Output: None

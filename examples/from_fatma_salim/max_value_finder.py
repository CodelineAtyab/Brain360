def find_max_value(numbers):
   
    if not numbers:
        return None

   
    max_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num

    return max_value

scores = [78, 92, 56, 99, 85]
temperatures = [-2, -8, -1, -5]
no_values = []

print(find_max_value(scores))        
print(find_max_value(temperatures))  
print(find_max_value(no_values))     
def sum_list_elements(numbers):
    total_sum = 0  
    for num in numbers:
        total_sum += num  
    return total_sum



data_points = [10, 20, -5, 3.5, 0]
print("Sum of data_points:", sum_list_elements(data_points))  
empty_list = []
print("Sum of empty_list:", sum_list_elements(empty_list))   
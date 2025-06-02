#User Story: Create Even Number Filtering Function
def get_even_numbers(numbers):
    even_num = []  
    for number in numbers: 
        if number % 2 == 0: 
            even_num.append(number) 
    return even_num

numbers = [1,2,3,4,5,6,7,8,9,10]
result = get_even_numbers(numbers)

print('Output:', result)
print("The original list:", numbers) 


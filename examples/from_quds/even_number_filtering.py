#User Story: Create Even Number Filtering Function
numbers = []
num = int(input("Enter the range of the list: "))
for i in range(num):
    user_input = int(input("enter the numbers: "))
    numbers.append(user_input)
def get_even_numbers(numbers):
    even_num = []  
    for number in numbers: 
        if number % 2 == 0: 
            even_num.append(number) 
    return even_num


result = get_even_numbers(numbers)

print('Output:', result)
print("The original list:", numbers) 


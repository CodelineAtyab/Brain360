#Develop List Summation Function

input_string = input("Enter numbers separated by commas: ")
input_list = input_string.split(",")

numbers = []
for num in input_list:
    numbers.append(int(num))

def summation_function(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

result = summation_function(numbers)
print("The sum of the numbers is:", result)

#Develop List Summation Function

def sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

numbers = input("Enter numbers separated by spaces: ")

if numbers.strip():
    number_list = [float(x) for x in numbers.split()]
else:
    number_list = []

print("Sum of the entered numbers:", sum(number_list))

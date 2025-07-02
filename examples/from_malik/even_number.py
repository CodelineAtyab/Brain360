def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
user_input = input("Enter numbers separated by commas: ")
numbers = [int(num.strip()) for num in user_input.split(",")]
result = get_even_numbers(numbers)
print(result)
#list for filtering even numbers

def Even_numbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input.split()]
even_numbers = Even_numbers(numbers)
print("The list of even numbers:", even_numbers)
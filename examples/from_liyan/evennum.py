def get_even_numbers(numbers):
    """
    This function takes a list of integers and returns a new list containing only the even numbers.
    The input list remains unchanged.
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


list_of_num = []

while True:
    i_said = input("Write down numbers and enter 'exit' to view even numbers: ")
    
    if i_said == 'exit':
        break
    
    number = int(i_said)
    list_of_num.append(number)
    print("Please enter a valid number or 'exit' to quit.")

even_numbers_list = get_even_numbers(list_of_num)

for num in even_numbers_list:
    print("Even number:", num)

def get_even_numbers(numbers):
    """
    Takes a list of integers and returns a new list containing only the even numbers.
    The input list remains unchanged. If the input list is empty or contains no even numbers,
    returns an empty list.
    """

    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


list_of_num = []

while True:
    i_said = input("Write down numbers and enter 'exit' to view even numbers: ")
    
    if i_said == 'exit':
        break
    
    try:
        number = int(i_said)
        list_of_num.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer or 'exit'.")

even_numbers_list = get_even_numbers(list_of_num)

if not even_numbers_list:
    print("No even numbers were found. Empty list:", even_numbers_list)
else:
    print("Even numbers:", even_numbers_list)


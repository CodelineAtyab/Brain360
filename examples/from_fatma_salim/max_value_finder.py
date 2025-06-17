def find_max_value(numbers):
   
    if not numbers:
        return None

    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number

    return max_value


user_input = input("Enter numbers separated by spaces: ")

try:
    number_list = [float(num) for num in user_input.split()]
except ValueError:
    print("Please enter only valid numbers.")
    exit()

max_number = find_max_value(number_list)

if max_number is not None:
    print("The maximum number is:", max_number)
else:
    print("You entered an empty list.")
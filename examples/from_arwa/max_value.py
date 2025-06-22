def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value

while True:
    user_input = input("Enter numbers separated by spaces: ")
    try:
        numbers = list(map(int, user_input.split()))
        break 
    except ValueError:
        print("Please enter only integers, separated by spaces. Try again.")

print("inputted list: ",numbers)
print("The maximum value is:", find_max_value(numbers))

#declaration
def sum_numbers(numbers):
    """
    Accepts a list of numbers and returns the sum. 
    """
    if not numbers: 
        return 0
    return sum(numbers)


numbers_list = []
#input 
while True:
    user_input = input("Enter numbers to sum them (type 'sum' to stop and sum): ")
#processing input 
    if user_input.lower() == 'sum':
        break
    try:
        number = float(user_input)
        numbers_list.append(number)
    except ValueError:
        print("Please enter a valid number!!!!!!.")

result = sum_numbers(numbers_list)
#print
print(f"The sum is: {result}")
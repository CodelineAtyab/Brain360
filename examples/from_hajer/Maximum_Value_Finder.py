#Implement Maximum Value Finder Function
def max_finder(numbers):
    if numbers == []:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

values= input("Enter random values separated by spaces: ")

if values == "":
    print("You didn't enter any value!")
else:
    number_list = []
    parts = values.split()
    for item in parts:
        number_list.append(float(item))
    maximum = max_finder(number_list)
    print("The maximum value is =", maximum)

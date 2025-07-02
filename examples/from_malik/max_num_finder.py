numbers = []

user_input = input("Enter numbers separated by commas: ")

for x in user_input.split(','):
    numbers.append(int(x.strip()))

max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print("The maximum number is:", max_value)
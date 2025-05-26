def find_max_value(numbers):
   
    if not numbers:
        return None

    max_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num

    return max_value

print("Find the largest number in a list.")

n = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(n):
    value = float(input(f"Enter number {i+1}: "))
    numbers.append(value)


result = find_max_value(numbers)

if result is None:
    print("The list is empty. No maximum value.")
else:
    print("The maximum number is:", result)
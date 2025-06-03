def find_max_value(numbers):
    if numbers == []:
        return None

    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest


data = input("Put some numbers separated by commas: ")
items = data.split(",")
nums = []

for n in items:
    nums.append(int(n)) 


result = find_max_value(nums)

if result is None:
    print("The list was empty.")
else:
    print("The biggest number is:", result)

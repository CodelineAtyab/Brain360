def find_max_value(numbers):
    if numbers == []:
        return None

    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

data = input("Put some numbers separated by commas: ")

if data == "":
    print("The list is empty.")
    nums = []
else:
    nums = []
    parts = data.split(",")
    for i in parts:
        nums.append(int(i))

    result = find_max_value(nums)
    print("The biggest number is:", result)

print("Original list:", nums)

nums = []

user_input = input("Enter a list of numbers (separated by commas): ")
parts = user_input.split(',')
for i in parts:
    nums.append(int(i))

def even_nums(numbers):
    list_of_even_nums = []
    for i in numbers:
        if i % 2 == 0:
            list_of_even_nums.append(i)
    return list_of_even_nums

result = even_nums(nums)
print("Result (even numbers):", result)
print("Original list:", nums)

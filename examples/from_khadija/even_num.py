# Declaration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Process
def get_even_numbers(nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens

even_numbers = get_even_numbers(numbers)

# Output
print(even_numbers)     # [2, 4, 6, 8, 10]
print(numbers)          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



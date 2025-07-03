def find_max_value(nums):
    if not nums:
        return None
    max_val = nums[0]
    for n in nums[1:]:
        if n > max_val:
            max_val = n
    return max_val

data = list(map(float, input("Enter numbers separated by spaces: ").split()))

print("Maximum value:", find_max_value(data))
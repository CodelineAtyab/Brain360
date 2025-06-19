nums = int(input("What is the num of row you want? "))
nums = abs(nums)
for num in range(1, nums+1):
    s = nums - num
    print(" " * s + "*" * ((2*num)-1))
  
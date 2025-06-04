def count_evens(nums):
  count_even =0
  for n in range(len(nums)):
    if nums[n] %2== 0 :
      count_even +=1
  return count_even
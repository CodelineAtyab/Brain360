list_of_nums=[]
def maximum_value(list_of_nums):
    n = int(input("enter the length of the list: "))
    for i in range(n):
        num = int(input("Enter a number: "))
        list_of_nums.append(num)
    if list_of_nums==[]:
        return None
    else:
        max_value=list_of_nums[0]
        for num in list_of_nums:
            if num>max_value:
                max_value = num
        print(max_value)
maximum_value(list_of_nums)

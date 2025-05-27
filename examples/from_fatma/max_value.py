list_of_nums=[]
def maximum_value(list_of_nums):
    while True:
        num = input("Enter a number, enter (done) to exit: ")
        if num == 'done':
            if list_of_nums==[]:
                return None
            else:
                print(max_value)
                break
        else:
            list_of_nums.append(int(num))
            max_value=list_of_nums[0]
            for num in list_of_nums:
                if num>max_value:
                    max_value = num      
maximum_value(list_of_nums)
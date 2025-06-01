list_of_nums=[]

while True:
    num = input("Enter a number, enter (done) to exit: ")
    if num != 'done':
        list_of_nums.append(int(num))
    else:
        break
               
def maximum_value(lst):
    if lst==[]:
        print(None)
    else:
        max_value=lst[0]
        for num in lst:
            if num>max_value:
                max_value = num
        print(max_value)
          
maximum_value(list_of_nums)
my_list=[]
def reverse_func(my_list):
    n = int(input("enter the length of your list: "))
    for i in range(n):
        data = input("enter a data of list: ")
        my_list.append(data)
    if my_list ==[]:
        print(my_list)
    else:
        new_list=[]
        for i in my_list[::-1]:
            new_list.append(i)
        print(new_list)

reverse_func(my_list)
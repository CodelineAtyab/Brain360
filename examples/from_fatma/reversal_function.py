my_list=[]

while True:
    data = input("enter a data to the list OR enter (done) to exit: ")
    if data != "done":
        my_list.append(data)
    else:
        break

def reverse_func(lst):
    if lst ==[]:
        print(my_list)
    else:
        new_list=[]
        for i in lst[::-1]:
            new_list.append(i)
        print(new_list)

reverse_func(my_list)

my_list=[]

while True:
    data = input("enter a data to the list OR enter (done) to exit: ")
    if data != "done":
        my_list.append(data)
    else:
        print("The original list: ",my_list)
        break

def reverse_func(lst):
    if lst ==[]:
        print("your list is empty.")
    else:
        new_list=[]
        for i in lst[::-1]:
            new_list.append(i)
        print("The reversed list: ",new_list)

reverse_func(my_list)

my_list = []

while True:
    user_input = input("Enter the elemnts write [done ] when you finish: ")
    if user_input != "done":
        my_list.append(user_input)
    else:
        break


def reverse_my_list(my_list):
    new_list = []
    for i in my_list[::-1]:
        new_list.append(i)
    return new_list
          
print("The original list:", my_list)
print("The reversed list: ",reverse_my_list(my_list))

# def reverse_my_list(my_list):
#      new_list = my_list[::-1]
#      print(new_list)

# reverse_my_list(my_list)







       


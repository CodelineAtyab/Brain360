my_data = []

while True:
    user_input = input("Enter the elemnets[write done when you finish]: ")
    if user_input != "done":
        my_data.append(user_input)
    else:
        break

element_to_count = input("Enter the elemnts: ")



def element_fre(my_data,element_to_count):
    count = 0
    if my_data == []:
        print(count)
    else:
        for i in my_data:
            if i == element_to_count:
                count +=1
    print(count)

element_fre(my_data,element_to_count)
    

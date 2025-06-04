#Develop  list  summation function 
list_of_numbers = []

while True:
    user_inputs = input("Enter the numbers writ(done)to exit: ")

    if user_inputs != "done":
        list_of_numbers.append(float(user_inputs))
    else:
        break


def sum_list_elements(data_points):
    total_sum = 0
    if data_points != []:
        for i in data_points:
            total_sum += i
    else:
        print("List is empty:",data_points)
    return total_sum

print("total_sum = ",sum_list_elements(list_of_numbers))
    
                    

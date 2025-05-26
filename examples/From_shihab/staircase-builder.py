num_of_row =int(input("Enter the number of row: "))

for i in range(1,num_of_row+1):
    flip_result =("%" + str(num_of_row) + "s") % ("#" *(i))
    print(flip_result)
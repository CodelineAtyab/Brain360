num_of_rows = int(input("enter the number of rows please!"))
for i in range(1,num_of_rows +1):
    print(" " * (num_of_rows - i ) , end="")
    print("#" * i  )

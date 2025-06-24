outer_counter = 0
rows_number = int(input("please add rows"))
while outer_counter < rows_number:
    inner_counter = 0
    while inner_counter < rows_number:
        print("*" , end="")
        inner_counter= inner_counter + 1
    print("")
    outer_counter = outer_counter + 1
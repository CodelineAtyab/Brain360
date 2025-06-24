num_of_rows = int(input("enter the number of rows please! "))
for i in range(1,num_of_rows+1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
num = int(input("Enter the number of rows (POSITIVE): "))
if num>0:
    for i in range(num):
        print('*'*num)
else:
    print("Please Enter a POSITIVE number.")
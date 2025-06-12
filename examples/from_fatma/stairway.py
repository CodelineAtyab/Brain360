num = int(input("Enter a number of rows (positive): "))
if num>0:
    for i in range(num):
        for j in range(i+1):
            print('*',end=' ')
        print('')
else:
    print("Enter a positive number.")

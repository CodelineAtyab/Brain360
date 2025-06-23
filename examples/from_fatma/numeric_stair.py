n = int(input("Enter the number of rows: "))
if n>0:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print('')
else:
    print("Enter a positive number.")
n = int(input("Enter the number of rows (POSITIVE): "))
if n>0:
    for i in range(1,n+1):
        print(' '*(n-i)+'*'*(2*i-1))
else:
    print("Enter a positive number.")
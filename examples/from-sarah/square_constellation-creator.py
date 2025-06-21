rownum = int(input("Enter number of rows needed: "))
if rownum> 0:
    for _ in range(rownum):
        print("* " * rownum)
else:
    print("Please enter a positive number.")

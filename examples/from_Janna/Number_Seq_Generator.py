x = int(input("Please Enter the Number of Rows (Positive Value!): "))
if x > 0:
    for i in range(1,x + 1):
        for j in range(1,i + 1):
            print(j, end="")
        for j in range(i - 1,0,-1):
            print(j, end="")
        print()
else:
    print("Invalid Value!")


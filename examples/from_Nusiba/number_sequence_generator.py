num = int(input("Enter the number of row:"))
# while is true...
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="" )
    for j in range(i - 1, 0, -1):
        print(j, end = "")
    print()
    


        
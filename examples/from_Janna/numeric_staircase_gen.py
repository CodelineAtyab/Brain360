n = int(input("Please Enter a Positive Integer: "))
if n > 0:
    for i in range(n + 1):
        for j in range(1,i + 1):
            print(j, end="")
        print()
else:
    print("Invalid Input! Please Enter a Positive Integer")
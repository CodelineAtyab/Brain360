n = int(input("Please Enter a Positive Integer: "))
if n > 0:
    for i in range(n):
        for j in range(n - i):
            print(" ", end = "")
        for j in range(2 * i + 1):
            print("*", end = "")
        print()
else:
    print("Invalid Input! Please Enter a Positive Integer")
n = int(input("Please Enter a Positive Integer: "))
if n > 0:
    for i in range(n):
        for j in range(n):
            print("*", end = "")
        print()
else:
    print("Invalid Value! Please Enter a Positive Integer")
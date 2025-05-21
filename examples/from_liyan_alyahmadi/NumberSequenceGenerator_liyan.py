rows = int(input("Enter a positive number: "))

if rows > 0:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
else:
    print("Please enter a number greater than 0.")

number_rows = int(input("Please enter a positive number(number of rows): "))
if number_rows > 0:
    for num1 in range(1, number_rows + 1):
        for num2 in range(1, num1 + 1):
            print(num2, end="")
        print("")
else:
    print("Invalid Input")
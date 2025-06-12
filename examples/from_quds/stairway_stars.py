number_of_rows = int(input("Please enter the number of rows(positive number): "))
if number_of_rows > 0:
    for count1 in range(number_of_rows):
        for count2 in range(count1 + 1):
            print("*", end="")
        print("")
else:
    print("Invalid Input")
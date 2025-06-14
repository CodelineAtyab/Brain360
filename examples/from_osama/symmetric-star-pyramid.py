positive_number = int(input("Please Enter a Positive Number: "))

for i in range(1, positive_number + 1):

    for spaces in range(positive_number - i):
        print(" ", end="")

    for add_star in range(i):
        print("*", end = " ")

    print("")
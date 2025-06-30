input_number = int(input("Enter the Positive Number: "))

if input_number > 0:
    for i in range(input_number):

        for s in range(input_number - i - 1):
            print(" ", end="")

        for j in range(i + 1):
            print("#", end="")
        print("")

else:
    print("[Error]: Please Add the Positive Number: ")
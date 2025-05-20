input_number = int(input("Enter the Positive Number: "))

if input_number > 0:
    for i in range(input_number):
        for j in range(i+1):
            print("#", end="")
        print("")


else:
    print("[Error]: Add the Positive Number Please")
    input_number = int(input("Enter the Positive Number: "))
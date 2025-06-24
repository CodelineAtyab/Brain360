numbers_entered = int(input("Please enter a positive number: "))

for i in range(1, numbers_entered + 1):
    for add_a_number in range(1, i + 1):
        print(add_a_number, end = "")
    print(" ")

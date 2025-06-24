"This is a triangle patren generator its so funzies have a look"
while True:
    try:
        user_input = int(input("Write a positive number: "))
        if user_input <= 0:
            print("Please enter a positive number greater than zero.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

for i in range(1, user_input + 1):
    for j in range(i):
        print("1", end="")
    print()

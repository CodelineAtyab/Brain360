x = int(input("Enter the Height of the Staircase (Positive Values Only): "))
if x > 0:
    for i in range(x + 1):
        print(" " * (x - i) + "#" * i)
else:
    print("Invalid Input!")
num_star_rows = int(input("Please enter the number of rows(poitive number): "))
if num_star_rows > 0:
    for nums in range(1, num_star_rows + 1):
        print(" " * (num_star_rows - nums), end="")
        print("*" * (2*nums - 1))
else:
    print("Invalid Input")
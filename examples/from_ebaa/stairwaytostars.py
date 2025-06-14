rows = int(input("Enter the number of rows: "))

if rows <= 0:
    print("Please enter a positive number!")
else:
    for i in range(1, rows + 1):
        stars = '*' * i
        print(stars)

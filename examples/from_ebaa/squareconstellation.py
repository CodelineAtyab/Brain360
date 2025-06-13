rows = int(input("Enter the number of rows: ")) 

if rows <= 0:
    print("Please enter a positive number!")
else:
    for i in range(rows):
        stars = '*' * rows
        print(stars)
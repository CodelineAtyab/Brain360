# Number Sequence Generator

number_of_rows=int(input("Input number of rows : ")) #asking the user 
if number_of_rows <= 0:
    print("Input a positive number")
else:
    for x in range(1, number_of_rows + 1):
        for y in range(1, x + 1):
            print(y, end='')
        for y in range(x - 1, 0, -1):
            print(y, end='')
        print()


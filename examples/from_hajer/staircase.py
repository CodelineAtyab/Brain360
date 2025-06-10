rows=int(input("Enter the number of the rows = "))
for n in range(1, rows + 1):
    print(' ' * (rows - n) + '#' * n)
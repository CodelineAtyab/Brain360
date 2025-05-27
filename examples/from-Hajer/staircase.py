rows=int(input("Enter the number of the rows = "))
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '#' * i)
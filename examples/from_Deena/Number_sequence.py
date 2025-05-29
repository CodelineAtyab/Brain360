number = int (input ("Input: "))
if number > 0:
    for a in range (1, number + 1):
        for b in range (1, a + 1 ):
            print (b, end= '')
        for b in range (a - 1, 0, -1 ):
            print (b, end='')
        print('')
else:
    print("Invalid Input")
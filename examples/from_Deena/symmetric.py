row = int (input ("Enter a number: "))
if row < 0:
    print ("No negative numbers accepted")
else:
    for i in range (1, row + 1):
        space = row - i
        star = 2 * i - 1
        print (" " * space + "*" * star)
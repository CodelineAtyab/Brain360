number = int (input ("Enter a number: "))
if number < 0:
    print ("No negative numbers accepted")
else:
    for i in range (number):
        for j in range (number):
            print ("*", end="")
        print ()
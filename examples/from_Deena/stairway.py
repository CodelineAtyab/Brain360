number = int(input("Enter a positive number: "))
if number < 0:
    print ("No negative numbers accepted")
else:
    for i in range (1, number + 1):
        print (i * "*")
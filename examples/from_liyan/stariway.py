"This Program Takes a Positive Integer and Turns It Into a Stairway Like Shape"



n = int(input("write a positive integer: "))

for i in range( n - 1):
    for j in range(i + 1 ):
        print("*", end=" " )
    print()
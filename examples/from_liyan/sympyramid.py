"This program takes a number and turns it into a pyramid"

p = int(input("write a positive integer: "))

for z in range(1, p + 1):
    for a in range(1, p - z + 1):
        print(" ", end='')
    for a in range(0, z):
        print("*", end=' ')

    print()
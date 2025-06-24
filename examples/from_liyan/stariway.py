"This Program Takes a Positive Integer and Turns It Into a Stairway Like Shape"

n = int(input("Please write down a positive intger: "))

for i in range(n):
    for j in range(i + 1 ):
        print("*", end=" ")
    print()
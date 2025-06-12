"This Program Takes a Positive Intger and turns it into a Numiric Staircase"

n = int(input("write a positive intger to see a numiric staircase: "))

for i in range(1, n+1):
    for j in range(1, i + 1 ):
        print(j, end="" )
    print()
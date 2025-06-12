#Stairway to stars

rows = int(input("Enter the number of rows:"))
i = 0
while i < rows:
    j = 0
    while j <= i:
        print("*", end=" ")
        j += 1
    print("")
    i += 1
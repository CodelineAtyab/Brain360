#Symmitric stars pyramid

rows = int(input("Enter the number of rows:"))
i = 0
while i < rows:
    j = 0
    while j < rows - i -1 :
        print(" ", end="")
        j += 1
    l = 0
    while l < 2 * i + 1:
        print("*", end="")
        l += 1
    print (" ")    
    i += 1


num = int(input("Type a number you like"))

for raw in range(1, num+1):
    for count in range(1, raw +1):
        print(count, end="")
    for count in range(raw-1 , 0 , -1):
        print(count , end="")
    print()
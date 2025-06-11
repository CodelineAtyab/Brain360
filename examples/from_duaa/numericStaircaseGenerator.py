nums = abs(int(input("Enter num of row you like : ")))
for num in range(1,nums+1):
    for num2 in range(1, num+1):
        print(num2 , end="")
    print()
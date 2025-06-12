while True:
    user_input = int(input("Enter Nuber Of Rows:"))
    if user_input<=0:
        print("Make Sure Number is Greater Than 0❗ ")
    else:
        break
for num in range(1,user_input +1):
    print("*"*num)
user_input = int(input("Enter numbers of rows [values should be positive]: "))
if user_input > 0:
    for i in range(1,user_input+1) :
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(1,i-1):
            print(j,end=" ")
        print()
else:
    print("invalid number try again")

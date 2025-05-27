num = int(input("Enter a number: "))
if num>0:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='')
        for j in range(i-1,0,-1):
            print(j,end='')
        print('')
else:
    print("please enter a positive number.")
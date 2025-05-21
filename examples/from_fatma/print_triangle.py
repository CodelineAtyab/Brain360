num_of_rows = int(input("Enter a number: "))
if num_of_rows>0:
    for i in range(num_of_rows):
        for j in range(i+1):
            print(1,end='')
        print('')
else:
    print("please enter a positive number!")
# user_input = int(input("Enter Number Of Row "))

while True:
    user_input = int(input("Enter Number Of Row "))

    if user_input <=0:
        print("Please Enter Number Greater Than 0 ")
    else:
        break


for r in range(user_input):
        number ="*" * (user_input)
        print(number)
                

    

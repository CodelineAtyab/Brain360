ask_user = int(input("enter your desired number of rows: "))
if ask_user > 0:
    for i in range(ask_user):
        print("*" * ask_user)
else:
    print("Wrong!, Enter a positive number!")



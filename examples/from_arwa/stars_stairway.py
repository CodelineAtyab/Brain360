user = input("please input a positive integer: ")

while not user.isdigit() or int(user) <= 0:
    print("invalid output, enter a positive number please")
    user = input("please input a positive integer: ")

number = int(user)

for i in range(1, number + 1):
    print("*" * i)
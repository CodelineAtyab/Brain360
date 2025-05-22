ask_user = int(input("Enter Valid number: "))

if not ask_user > 0:
    print("plz try to Enter Valid number(It must be >0)")

for num in range(1,ask_user + 1):
    for num2 in range(1, num+1):
        print(num2, end="")
    for num2 in range(num-1,0,-1):
        print(f"{num2}, end=\n")



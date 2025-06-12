count =0
while True:
    user_input = (input("Enter Numbers Of Rows:"))
    if user_input == "" :
        print("Mack Sure Without Space⚠️")
    elif int(user_input) <= 0 :
        print("Mack Sure You Enter The Number >0 ❗")
    else:
        break
for n in range(1,int(user_input) +1):
    for x in range(1, n +1):
        print(x, end="")
    print()
    
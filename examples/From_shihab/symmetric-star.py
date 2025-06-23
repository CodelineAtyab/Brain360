while True:
    user_input = (input("Enter Numbers Of Rows:"))
    if user_input == "" :
        print("Mack Sure Without Space⚠️")
    elif int(user_input) <= 0 :
        print("Mack Sure You Enter The Number >0 ❗")
    else:
        break
star_count = 1
for x in range(int(user_input)):
     spaces = int(user_input) - x - 1
     print(" " * spaces + "*" * star_count)
     star_count += 2 
     
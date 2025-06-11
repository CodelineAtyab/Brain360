


def user_input():
    list_num =[]
    while True:
        numbers = (input("Enter The List Of Number/(Done) to finsh: "))
        if numbers.lower() == "done":
            break
        elif numbers =="":
            print("No value added❗")
            return []
        else:
            list_num.append(int(numbers))
   
    

    bigger = max(list_num)
    print(f"Your Numbers Are: {list_num}")
    return bigger

last = user_input()

print("The largest number is:", last)


list_num =[]

#numbers = input("Enter The list of Number/(done) to finsh: ")

while True:
    numbers = (input("Enter The List Of Number/(Done) to finsh: "))
    if numbers.lower() == "done":
        break
    else:
        list_num.append(int(numbers))
print(list_num)
print(f"maximum number in the list is {max(list_num)}")
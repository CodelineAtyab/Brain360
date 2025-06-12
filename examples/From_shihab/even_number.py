origin_list = []
even_numbers =[]
while True:
    user_input = input("Enter The numbers/ Enter(Done) To exit: ")
    if user_input.lower() == "done":
        break
    else:
        origin_list.append(int(user_input))

def get_even_numbers():
    for n in origin_list:
        if n % 2 == 0:
            even_numbers.append(n)
       
    
    print(f"Your List are:{origin_list} ")
    return even_numbers


even_list = get_even_numbers()
print(f"The List Of Even Numbers are {even_list}")
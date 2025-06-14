def max_num():
    list_of_numbers = []
    
    while True:
        user_input = input("Add number or 'done' to finish: ")
        if user_input.lower() == 'done':
            break
        list_of_numbers.append(int(user_input))
    
    if not list_of_numbers:
        print("No numbers entered!")
        return None
    
    maximum_num = list_of_numbers[0]
    for num in list_of_numbers:
        if num > maximum_num:
            maximum_num = num
    
    print("Your numbers:", list_of_numbers)
    print("Highest number:", maximum_num)
    return maximum_num

max_num()
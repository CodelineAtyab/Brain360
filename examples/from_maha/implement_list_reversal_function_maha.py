def new_list():
    your_list = []
    reversed_list = []
    
    while True:
        add_things = input("add item to your list and done when you finshed ")
        if add_things.lower() != "done":
            your_list.append(add_things)
        else:
            break
    
    reversed_list = your_list[::-1]
    
    print("Your Orginal list is", your_list)
    print("your reseverd list is", reversed_list)
    
    return your_list, reversed_list

new_list()



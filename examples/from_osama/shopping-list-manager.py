cart = []
do = True

def add():
    inputted_item = str(input("Enter item to add and exit when you are done: "))
    cart.append(inputted_item)
    print(inputted_item, "is Added to the Cart")
    while inputted_item != "exit":
        inputted_item = str(input("Enter item to add and exit when you are done: "))
        if inputted_item == "exit":
            break
        cart.append(inputted_item)
        print(inputted_item, "is Added to the Cart")
            

def show():
    print("Your shopping list:")
    for i in cart:
        print ("-", i)


def remove():
    number_of_remove = str (input("Enter the item name to remove the item: "))
    cart.remove(number_of_remove)
    print("The removed item is", number_of_remove)
    print("The left items are:")
    for i in cart:
        print("-", i)


def clear():
    clear_input = str(input("Are you sure that you want to clear the cart (y/n)? "))
    if clear_input == "y":
        cart.clear
        print("The cart is clear")


def exit():
    exit = str(input("Are you sure that you want to exit (y/n)? "))
    if exit.lower == "y":
        print("Thanks!")



while do == True:
    print("Welcome to Shopping List Manager! \n 1. Add item \n 2. Remove item \n 3. Show list \n 4. Clear list \n 5. Exit")

    inputted_option = int(input("Enter the Option: "))
    if inputted_option == 1:
        add()
    elif inputted_option == 3:
        show()
    elif inputted_option == 2:
        remove()
    elif inputted_option == 4:
        clear()
    elif inputted_option == 5:
        exit()
        print("Thanks!")
        break
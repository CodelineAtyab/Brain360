

cart=[]


def add():
    while True:
        item = input("Enter an item to add: ")
        if item == "exit":
            break
        cart.append(item)
        print("added")

def rmv():
    while True:
        item = input("Enter an item to remove: ")
        if item == "exit":
            break
        cart.remove(item)
        print("removed")

def show():
    while True:
        # item = input("Your shopping list:").lower
        # if  item == "exit":
        #     break
        # else:
        print(cart)
        break


def clear():
    while True:
        item = input("Do you want to clear your list (yes/no)")
        if item == "yes":
            cart.clear()
            print("cart cleared")
            break
        elif item == "no":
            break

while True:
    print("Please pick an option")
    print("1. Add items to the shopping list")
    print("2. Remove items from the shopping list")
    print("3. Show my shopping list")
    print("4. Clear my shopping list")
    print("Type 'exit' to go back to options")
    print("Type 'end' to end exit the shopping list")

    option = input()
    if option == "1":
        add()
    elif option == "2":
        rmv()
    elif option == "3":
        show()
    elif option == "4":
        clear()
    elif option == "end":
        break

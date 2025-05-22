

cart=[]


def add():
    while True:
        item = input("Enter an item to add or 'exit' to go back to options menu: ")
        if item == "exit":
            break
        cart.append(item)
        print("Item has been added")

def rmv():
    while True:
        item = input("Enter an item to remove or 'exit' to go back to options menu: ")
        if item == "exit":
            break
        cart.remove(item)
        print("Item has been removed")

def show():
    while True:
        # item = input("Your shopping list:").lower
        # if  item == "exit":
        #     break
        # else:
        print("Your shopping list:")
        for num in range(len(cart)):
                print(f"{num + 1} . {cart[num]}")
        print("Type 'exit' to go back to options menu")
        back = input()
        print()
        if back == "exit":
            break


def clear():
    while True:
        item = input("Do you want to clear your list (yes/no)")
        if item == "yes":
            cart.clear()
            print("Your cart has been cleared")
            print("Type 'exit' to go back to options menu")
            back = input()
            if back == "exit":
                break
        elif item == "no":
            break

while True:
    print("Please pick an option")
    print("1. Add items to the shopping list")
    print("2. Remove items from the shopping list")
    print("3. Show my shopping list")
    print("4. Clear my shopping list")
    print("While inside an option type 'exit' to go back to options menu")
    print("While in options menu type 'end' to end exit the shopping list")

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

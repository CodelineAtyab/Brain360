shoppinglist = []
def add():
    itemNew = input("What item do you want to add to the Shopping list? ")
    shoppinglist.append(itemNew)
    print(f"'{itemNew}' added to the list:)\n")
def show():
    if not shoppinglist:
        print("List is empty.\n")
    else:
        print("Shopping List:")
        for i, itemNew in enumerate(shoppinglist, 1):
            print(f"{i}. {itemNew}")
        print()
def remove():
    if not shoppinglist:
        print("List is empty\n")
        return
    show()
    num = input("Enter the item number to remove: ")
    try:
        indexItem = int(num)
        if 1 <= indexItem <= len(shoppinglist):
            removed = shoppinglist.pop(indexItem - 1)
            print(f"'{removed}' removed from the list.\n")
        else:
            print("Invalid number:(\n")
    except ValueError:
        print(" Enter a valid number:(\n")
def clear():
    shoppinglist.clear()
    print("Shopping list is cleared\n")
print("Welcome to Shopping List Manager:)!")
running = True
while running:
    print("\n@@@@@@@@@")
    print("1. Add item")
    print("2. Show list")
    print("3. Remove item")
    print("4. Clear list")
    print("5. Exit")
    print("@@@@@@@@@")
    choice = input("Choose an option: ")
    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        remove()
    elif choice == "4":
        clear()
    elif choice == "5":
        print("Thank you for shopping with us:)!!")
        running = False
    else:
        print("Invalid choice\n")

shopping_list = []

def add_item():
    while True:
        item = input("Enter item to add or type (done) to stop: ")
        if item.lower() == "done":
            break
        else:
            shopping_list.append(item)
            print(f"'{item}' has been added to the list")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the list.")

def show_list():
    print("Shopping List:")
    i = 1
    for item in shopping_list:
        print(f"{i}. {item}")
        i += 1

def clear_list():
    shopping_list.clear()
    print("Shopping list cleared.")

def exit_manager():
    print("Exiting Shopping List Manager.")
    exit()

while True:
    print("\nWelcome to Shopping List Manager!")
    print("1. Add item\n2. Remove item\n3. Show list\n4. Clear list\n5. Exit")
    n = int(input("Choose an option: "))
    if n == 1:
        add_item()
    elif n == 2:
        remove_item()
    elif n == 3:
        show_list()
    elif n == 4:
        clear_list()
    elif n == 5:
        exit_manager()
    else:
        print("Invalid option. Please try again.")
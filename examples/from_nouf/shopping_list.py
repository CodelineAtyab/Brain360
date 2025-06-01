shopping_list = []
def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added to the list.")

def remove_item():
    if not shopping_list:
        print("The list is empty.")
        return

def show_list():
    if len(shopping_list) == 0:
        print("this shopping list is empty.")
    else:
        print("Your shopping list:")
        for i in range(len(shopping_list)):
            print(i + 1, "-", shopping_list[i])

def clear_list():
    shopping_list.clear()
    print("Shopping list is cleared.")

def run_shopping_list_manager():
    print("Welcome to shopping list manager")
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Show list")
        print("4. Clear list")
        print("5. Exit")

        choice = input("Choose from these options: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            show_list()
        elif choice == "4":
            clear_list()
        elif choice == "5":
            print("Bye")
            break
        else:
            print("its an invalid choice so please enter 1–5.")

run_shopping_list_manager()

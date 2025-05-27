shopping_list = []

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added.")

def remove_item():
    if shopping_list:
        for i in range(len(shopping_list)):
            print(f"{i + 1}. {shopping_list[i]}")
        number = input("Enter item number to remove: ")
        if number.isdigit():
            index = int(number) - 1
            if 0 <= index < len(shopping_list):
                removed = shopping_list.pop(index)
                print(f"'{removed}' removed.")
            else:
                print("Invalid number.")
        else:
            print("Please enter a valid number.")
    else:
        print("List is empty.")

def show_list():
    if shopping_list:
        print("Shopping list:")
        for i in range(len(shopping_list)):
            print(f"{i + 1}. {shopping_list[i]}")
    else:
        print("List is empty.")

def clear_list():
    shopping_list.clear()
    print("List cleared.")

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Clear list")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        show_list()
    elif choice == '4':
        clear_list()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Please enter a number from 1 to 5.")
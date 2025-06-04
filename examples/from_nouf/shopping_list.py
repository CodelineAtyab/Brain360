shopping_list = []

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added to the list.\n")

def remove_item():
    if len(shopping_list) == 0:
        print("There is nothing to remove because your shopping list is empty.\n")
        return

    num = input("Enter the item number to remove: ")

    if num.isdigit():
        index = int(num)
        if 1 <= index <= len(shopping_list):
            removed = shopping_list.pop(index - 1)
            print(f"'{removed}' removed from the list.\n")
        else:
            print("That number is not in the list.\n")

def show_list():
    if len(shopping_list) == 0:
        print("This shopping list is empty.\n")
    else:
        print("Your shopping list:")
        for i in range(len(shopping_list)):
            print(f"{i + 1} - {shopping_list[i]}")
        print()

def clear_list():
    shopping_list.clear()
    print("Shopping list is cleared.\n")

print("Welcome to Shopping List Manager!\n")
while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Show list")
        print("4. Clear list")
        print("5. Exit")

        choice = input("Choose from these options: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            show_list()
        elif choice == "4":
            clear_list()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

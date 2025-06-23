# Shopping list

shopping_list = []

def add_item():
    item = input("Add an item : ")
    shopping_list.append(item)
    print(f"The item is added to your shopping list: {item}")

def remove_item():
    print("Your Shopping list items :")
    i = 1
    for item in shopping_list:
        print(f"{i}. {item}")
        i += 1
    
    number = int(input("Choose the number of the item that you want to remove: "))
    if 1 <= number <= len(shopping_list):
        removed = shopping_list[number - 1]
        shopping_list[:] = shopping_list[:number - 1] + shopping_list[number:]
        print(f"The item is removed from your shopping list : {removed}")
    else:
        print("You entered an invalid number!")

def show_list():
    if shopping_list:
        print("\nYour shopping list items are :")
        # Manual indexing again
        i = 1
        for item in shopping_list:
            print(f"{i}. {item}")
            i += 1
    else:
        print("\nThe list is empty")

def clear_list():
    shopping_list.clear()
    print("\nThe list is cleared!")

while True:
    print("\n1: Add items\n2: Remove items\n3: Show list of items\n4: Clear shopping list\n5: Exit shopping list")
    choice = input("Choose an option : ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        show_list()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        print("Thank you ,Bye!")
        break
    else:
        print("You entered an invalid choice!")

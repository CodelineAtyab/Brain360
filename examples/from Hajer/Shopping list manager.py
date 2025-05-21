shopping_list = []

while True:
    print("Welcome to your shopping list!\n1. Add item\n2. Remove item\n3. Show list\n4. Clear list\n5. Exit")
    
    option =input("Choose an option : ")

    if option == '1':
        item = input("Enter item: ")
        shopping_list.append(item)
        print("Item added.\n")

    elif option == '2':
        if shopping_list:
            for i in range(len(shopping_list)):
                print(f"{i + 1}. {shopping_list[i]}")
            try:
                num = int(input("Item number to remove: "))
                if 1 <= num <= len(shopping_list):
                    shopping_list.pop(num - 1)
                    print("Item removed.\n")
                else:
                    print("Invalid item number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
        else:
            print("The list is empty. Nothing to remove.\n")

    elif option == '3':
        if shopping_list:
            print("Your shopping list:")
            for i in range(len(shopping_list)):
                print(f"{i + 1}. {shopping_list[i]}")
            print()
        else:
            print("\nYour shopping list is empty.\n")

    elif option == '4':
        shopping_list = []
        print("List cleared.\n")

    elif option == '5':
        print("Goodbye!")
        break

    else:
        print("Unavailable choice.\n")

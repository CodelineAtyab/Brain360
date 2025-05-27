shopping_list = []
print("Welcome to Shopping List Manager!")
while True:
    options = input("1. Add item \n 2. Remove item \n 3. Show list \n 4. Clear list \n 5. Exit \n Choose an option:")
    if options == "1":
        add_items = input("Enter item to add: ")
        shopping_list.append(add_items)
    elif options == "2":
        item_to_remove = input("Enter the item you want to remove: ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"{item_to_remove} was removed.")
        else:
            print(f"{item_to_remove} is not in the list.")
        print("Updated shopping list:", shopping_list)
    elif options == "3":
        print ("The shopping list: " , shopping_list)
    elif options == "4":
        shopping_list.clear()
        print("Shopping list has been cleared.")
    elif options.lower() == '5' or "eixt":
        break

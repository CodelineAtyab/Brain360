shopping_list = []


while True:
    print("  Shopping List Menu: ")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")

    choice = input("Choose a number from 1 to 5: ")

    if choice == "1":
        while True:
            item = input("What do you want to add to the list: ")
            if item.lower() == "done":
                break
            else:
                shopping_list.append(item)
                #print("your shopping_list is: ")

    elif choice == "2":
        item = input("What do you want to remove from the list: ") 
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print(item, "is not in the list.")

    elif choice == "3":
        print("Your shopping list:")
        count=1
        for item in shopping_list:
            print(count, "-",item)
            count_1+=1

    elif choice == "4":
        shopping_list.clear()
        print("Your list has been cleared.")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        

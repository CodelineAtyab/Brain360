shopping_list = []
print("Welcome to Shopping List Manager!")
print("1. Add item\n2. Remove item\n3. Show list\n4. Clear list\n5. Exit")
while True:
    n = int(input("Choose an option: "))
    if n == 1:
        while True:
            item = input("Enter item to add or type (done) to stop: ")
            if item.lower() == "done":
                break
            else:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list")

    elif n == 2:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' not found in the list.")

    elif n == 3:
        print("Shopping List:")
        i = 1
        for item in shopping_list:
            print(f"{i}. {item}")
            i += 1
        
    elif n == 4:
        shopping_list.clear()
        print("Shopping list cleared.")

    elif n == 5:
        print("Exiting Shopping List Manager.")
        break

    else:
        print("Invalid option. Please try again.")
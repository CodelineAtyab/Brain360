shopping_List = []

# Add Item

while True:
    print("Welcome to Shopping List Mangeer!") 
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Clear List")
    print("5. Exit")

    option = int(input("Choose an Option: "))

    if option == 1:
        item = input("Enter to add: ")
        shopping_List.append(item)
        print(item, "added to the list. ")
    elif option == 2:
        item_to_remove = int(input("Enter Item number to Remove"))
        index = shopping_List[item_to_remove -1]
        shopping_List.remove(index)
        print(index, "Removed from list")
    elif option == 3:
        for item in shopping_List:
            print(item)
    elif option == 4:
        shopping_List.clear()
        print("Your List is Empty")
    elif option == 5:
        break
    else:
        print("Please Choose 1 to 5 Only!")        
    
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
            count+=1

    elif choice == "4":
        shopping_list.clear()
        print("Your list has been cleared.")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        
        
                
'''
shopping_list = []

def show_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1 to 5): ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added.")
    
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item,"has been removed.")
        else:
            print(item , " is not in the list.")
    
    elif choice == "3":
        if shopping_list:
            print("\nCurrent Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("Shopping list is empty.")
    
    elif choice == "4":
        shopping_list.clear()
        print("All items cleared.")
    
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a number from 1 to 5.") '''






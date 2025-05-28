shopping_list = []

while True:
    print("\nHI ")
    print("1. add")
    print("2. remove")
    print("3. show the whole list")
    print("4. clear")
    print("5. exit")
    
    item = input("What do you want to do? ").lower()

    if item == "1":
        item = input("Enter your shopping item (when you finish enter 'exit'): ").lower()
        shopping_list.append(item)
        print(f"'{item}' added.")
    
    elif item == "2":
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' Its not found in the list.")

    elif item == "3":
        print("Your shopping list:", shopping_list)

    elif item == "4":
        shopping_list.clear()
        print("Shopping list cleared.")

    elif item.lower() == "5":
        break




        

    
    



    



 







shopping_list = []

while True:
    print("\nHI ")
    print("1. add")
    print("2. remove")
    print("3. show the whole list")
    print("4. clear")
    print("5. exit")
    
    user_input = input("What do you want to do? ").lower()

    if user_input == "1":
        item = input("Enter your shopping item (type 'exit' to cancel): ").strip()
        if item.lower() != "exit":
            shopping_list.append(item)
            print(f"'{item}' added.")

    elif user_input == "2":
        item_to_remove = input("Enter the item you want to remove: ").strip()
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"'{item_to_remove}' removed.")
        else:
            print(f"'{item_to_remove}' is not in the list.")

    elif user_input == "3":
        if shopping_list:
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"item {i}: \"{item}\"")
        else:
            print("Your shopping list is empty.")

    elif user_input == "4":
        shopping_list.clear()
        print("Shopping list cleared.")

    elif user_input == "5":
        print("Goodbye!")
        break
    




        

    
    



    



 







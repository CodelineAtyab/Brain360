shopping_list = []

while True:
    print("\nHI ")
    print("1. add")
    print("2. remove")
    print("3. show the whole list")
    print("4. clear")
    print("5. exit")
    
    User_Input = input("What do you want to do? ").lower()

    if User_Input == "1":
        item = input("Enter your shopping item (when you finish enter 'exit'): ").lower()
        shopping_list.append(item)
        print(f"'{item}' added.")
    
    elif User_Input == "2":
        item_to_remove = input("Enter the item you want to remove: ")
        if item_to_remove in shopping_list:
          shopping_list.remove(item_to_remove)
          print(f"'{item_to_remove}' removed.")
        else:
          print(f"'{item_to_remove}' is not in the list.")

    elif User_Input == "3":
        if shopping_list:
          print("Your shopping list:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"item {i}: \"{item}\"")
        else:
          print("Your shopping list is empty.")

    elif User_Input == "4":
        shopping_list.clear()
        print("Shopping list cleared.")

    elif User_Input.lower() == "5":
        break




        

    
    



    



 







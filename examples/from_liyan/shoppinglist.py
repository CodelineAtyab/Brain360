shopping_list = []


while True:
 user_add = input("Add iteams to your list or type 'show' 'remove' 'clear' 'exit' : ")
 shopping_list.append(user_add)


 if user_add == "show":
    print(shopping_list)

 elif user_add == "remove":
        item_to_remove = input("What item do you want to remove? ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"Removed {item_to_remove} from your list.")
        else:
            print(f"{item_to_remove} not found in your list.")

 elif user_add == "clear":
   clear= shopping_list.clear()
   print(clear)

 elif user_add == "exit":
     print(" exiting shopping list!!")

 else:
        shopping_list.append(user_add)
        print(f"Added {user_add} to your shopping list.")
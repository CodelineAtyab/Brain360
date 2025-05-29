shopping_list = []

while True:
 user_thought = input("what do you want to do 'add' , 'remove' , 'show' , 'clear' ")

 if user_thought == "add":
        user_item = input("Add item to your list (or type 'stop' to exit adding): ")
        while user_item.lower() != "stop":
            shopping_list.append(user_item)
            print(f"{shopping_list} — item added to your list!")
            user_item = input("Add another item (or type 'stop' to finish adding): ")

 elif user_thought == "remove":
    user_item = input("Enter the item to remove: ")
    if user_item in shopping_list:
        shopping_list.remove(user_item)
        print(f"'{user_item}' removed from your list.")
    else:
        print(f"'{user_item}' is not in your list.")

 elif user_thought == "show":
    print(shopping_list)
 elif user_thought == "clear":
    clear = shopping_list.clear(user_list)
    print(clear)

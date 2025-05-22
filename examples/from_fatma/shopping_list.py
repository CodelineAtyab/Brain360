shopping_list=[]

while True:
    print("Welcome to shopping list manager!")
    print("1. Add item\n2. Remove item\n3. Show list\n4. Clear list\n5. Exit")
    option=int(input("Choose an option: "))
    if option==1:
        item=input("Enter item to add: ")
        print(f"'{item}' added to the list.")
        shopping_list.append(item)
    elif option==2:
        item_remove=int(input("Enter item number to remove: "))
        x = shopping_list[item_remove-1]
        shopping_list.remove(shopping_list[item_remove-1])
        print(f"'{x}' , removed from the list.")
    elif option==3:
        print("Your shopping list: ")
        for i in range(len(shopping_list)):
            print(f"{i+1}. {shopping_list[i]}")
    elif option==4:
        shopping_list.clear()
        print("shopping list: ",shopping_list)
    else:
        break
shopping_list = []
while True :
    user_ask = int(input("enter option number 1. Add item  " 
"2. Remove item " 
" 3. Show list  " 
" 4. Clear list "
" 5. Exit : "))
    
    if user_ask == 1:
        while True:
            user_input = input("enter your item when you finish enter [done]: ").lower()
            if user_input =="done":
                break
            else :
                shopping_list.append(user_input)
        
    elif user_ask == 2:
            user_remove = int(input("enter item number to remove: "))
            user_remove_value =int(len(shopping_list) - user_remove)
            for user_remove_value in shopping_list[user_remove_value] :
                shopping_list.pop(shopping_list[user_remove_value])
                print(f"{shopping_list[user_remove_value]} removed from list.")
            else:
                print(f"{user_remove} not found items")

    print("\nYour shopping list:")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")
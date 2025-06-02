#Task 4 Shopping list
shopping_list = []
print("Welcome to Shopping List Manager!")
#the user need to choose on of these options 
print("1. Add item\n2. Remove item\n3. Show-list\n4. Clear-List\n5. Exit")
choices_op = ["1. Add item\n2. Remove item\n3. Show-list\n4. Clear-List\n5. Exit"]

while True:
    choices_op = int(input("Choose the option (Add item,...): "))
    if choices_op  == 1: #Adding items
        while True:
                items_list = input("Write you list (type done of you finish): ").lower()
                if items_list == "done":
                    break   
                else:
                 shopping_list.append(items_list)
                 print(f"The added items: {shopping_list}")
                
    elif choices_op == 2: #Remove item
        items = int(input("Enter the itemes that you want to remove: "))
        if 0 <= items < len(shopping_list):
            remove_item = shopping_list.pop(items)
            #shopping_list.remove(items)
            print(f"{remove_item}. is  removed")

        else:
            print(f"{items} is not found in the list")

    elif choices_op == 3: #Show-list
        print("The shopping list: ")
        count = 1
        for items in shopping_list:
            print(f"{count}. {items}")
            count += 1

    elif choices_op == 4: #Clear-List
        shopping_list.clear()
        print("THe shopping list is cleared")
    
    elif choices_op == 5: #Exit
        print("Exiting the shopping list")
        break
    else:
        print("Invalid. try again.")
            
    
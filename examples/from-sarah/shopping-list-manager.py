shopping_list = []
running = True  # We'll control the loop with this

print("Welcome to Shopping List Manager!")
def add():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print("'" + item + "' added to the list.")
def remove():
    if len(shopping_list) == 0:
            print("List is empty.")
    else:
            print("Items in your shopping list:")
            for i in range(len(shopping_list)):
                print(str(i + 1) + ". " + shopping_list[i])

            choice_to_remove = input("Enter the number of the item to remove: ")

            if choice_to_remove.isdigit():
                index = int(choice_to_remove) - 1
                if 0 <= index < len(shopping_list):
                    removed_item = shopping_list.pop(index)
                    print("'" + removed_item + "' removed from the list.")
                else:
                    print("Invalid number.")
            else:
                print("Please enter a valid number.")

def show():
     if len(shopping_list) == 0:
            print("Your list is empty.")
     else:
            print("Your shopping list:")
            for i in range(len(shopping_list)):
                print(str(i + 1) + ". " + shopping_list[i])

def clear():
      shopping_list = []
print("Shopping list cleared.")

def exit():
     print("Goodbye!")
 # Ends the loop without using 'break'


while running:
    print()
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Clear list")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add()


    elif choice == "2":
        remove()
        

    elif choice == "3":
        show()

    elif choice == "4":
       clear()

    elif choice == "5":
        exit()
        running = False 

    else:
        print("Please enter a number from 1 to 5.")

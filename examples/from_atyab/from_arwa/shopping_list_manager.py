# Functions 

def add_items(option):
    if option == 1:
        add_item = input("Enter item to add: ")
        items.append(add_item)
        print(f'"{add_item}" added to the list')

def remove_items(option):
    index_number = int(input("Enter item number to remove: ")) - 1
    print(f'{items[index_number]}'' removed from the list.\n' )
    items.pop(index_number)

def show_list(option):
    if option == 3:
        print("Your shopping list:")
        for index, item in enumerate(items, start=1):
            print(index,".", item)
        
def clear_list(option):
    if option == 4:
        items.clear()
        print(items)

#Processs

items = []

while True:
    print("\nWelcome to Shopping List Manager! \n1. Add item \n2. Remove item\n3. Show list \n4. Clear list \n5. Exit ")
    option = int(input("Choose an option:"))
    if option == 1:
        add_items(option)
    if option == 2:
        remove_items(option)
    elif option == 3:
        show_list(option)
    elif option == 4:
        clear_list(option)
    elif option == 5:
        break

    
# Call the function
# add_items(option)
# clear_list(option)
# remove_items(option)
# show_list(option)
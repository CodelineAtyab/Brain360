list = []
print("Welcome to Shopping List Manager!")
print("1. Add item \n2. Remove item \n3. Show list \n4. Clear list \n5. Exit")
choise = int(input("Choose an option: "))
if choise == 1:
    item = str(input("Enter item to add: "))
    list.append(item)
    print(f"'{item}' added to the list.")
    
        


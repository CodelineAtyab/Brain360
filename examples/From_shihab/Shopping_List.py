print("Welcome To Shopping List Manager🤍🤖 ..")
list_items=[]

#print("1 for add, 2 for remove, 3 for show yor list, 4 clear all item\n")
#choose=int(input("Enter Thr number: "))


#Adding item ..
def add_item():
    while True:
        item =input("PLZ Enter your Items: ")
        if item == "done":
            break

        else:
            list_items.append(item)
    

def remove():
    while True:
        item_remove= input("Do you want to remove something?(item name)")
        if item_remove == "done":
            break
        elif item_remove in list_items:
            list_items.remove(item_remove)
            print(f"{item_remove}, is removed")
        else:
            print("The item not found")

def show_list():
    count= 1
    print("This Your List📃")
    for item in list_items:
        print(count,"-", item)
        count +=1
        print("_"*10)
      
        
    

def clear_list():
    list_items.clear()
    print("The List cleared")

def exit():
    leav=input("Enter Yes To Exit: ")
    if leav.lower() == "yes":
        print("GOOD^_^BYE")

   



while True:
    print(" 1 For Add\n 2 For Remove\n 3 for Show Your List\n 4 Clear All Item\n 5 Exit")
    choose=input("Enter Thr number: ")
    

    if choose == "1":
        add_item()
    elif choose == "2":
        remove() 
    elif choose == "3":
        show_list()
        
    elif choose == "4":
        clear_list()
    elif choose == "5":
        exit()
        break
    
    
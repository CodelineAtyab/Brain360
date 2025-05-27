shopping_list=[]

print ("\n1. add item") # \n for new line 
print ("2. remove item")
print ("3. show list ")
print ("4. clear list ")
print ("5. exit ")

while True :
   
    choice = input("enter number: ")
    if choice == "1":
      item= input("enter your item to add : ")
      shopping_list.append(item)
      print (" item added ! ")

    elif choice == "2":
     if shopping_list:
        print("Your shopping list:")
        for item in shopping_list:
            print("- " + item)
        item_to_remove = input("Enter item name to remove: ")
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"'{item_to_remove}' removed from the list.")
        else:
            print("Item not found in the list.")
     else:
         print("List is empty.")
    

    elif choice == "3":
     if shopping_list:
        print("Your shopping list:")
        for item in shopping_list:
            print("- " + item)
     else:
        print("List is empty.")


    elif choice == "4":
        shopping_list = []
        print("List cleared.")

    elif choice == "5":
       print (" goodbye !")
       break 
    else :
       print ("enter valid number please ...!")
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
            for i in range(len(shopping_list)):
                print(f"{i + 1}. {shopping_list[i]}")
            index = int(input("Enter item number to remove: "))
            if 1 <= index <= len(shopping_list):
                removed = shopping_list.pop(index - 1) # pop is used to remove item from shopping list  
                print(f"'{removed}' removed from the list.")
            else:
                print("Invalid number.") 
         
        else:
            print("List is empty.")

    elif choice == "3":
        if shopping_list:
            print("Your shopping list:")
            for i in range(len(shopping_list)):
                print(f"{i + 1}. {shopping_list[i]}")
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
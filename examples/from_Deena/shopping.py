shopping_list = []
print ("Welcome to Shopping List Manager!")
while True:
    print ("1. Add Item")
    print ("2. Remove Item")
    print ("3. Show List")
    print ("4. Clear List")
    print ("5. Exit")


    option = input ("Enter an option (1-5): ")

    if option == "1":
       item = input ("Enter item to add: ")
       shopping_list.append (item)
       print ( item, " added to the list.")

    elif option == "2":
      item = int (input ("Enter item number to remove: "))
      print (shopping_list[item-1], " Removed from the list.")
      shopping_list.remove (shopping_list[item-1])
      print(shopping_list)


    elif option == "3":
       for item in shopping_list:
          print (item)

    elif option == "4":
       shopping_list.clear ()
       print ("Shopping list cleared.")

    elif option == "5":
       print ("Goodbye!")
       break

    else:
       print ("Invalid option. Please enter a number from 1 to 5.")
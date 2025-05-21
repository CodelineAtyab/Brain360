shopping_list=[]

print("\n1. add item") # \n for new line 
print("2. show list ")
print("3. exit ")

while True :
   
    choice = input("enter number: ")
    if choice == "1":
      item= input("enter your item to add : ")
      shopping_list.append(item)
      print (" item added ! ")

    elif choice == "2":
       print ("shopping list :")
       for item in shopping_list:
        print ("-" + item)

    elif choice == "3":
       print (" goodbye !")
       break 
    else :
       print ("enter valid number please ...!")
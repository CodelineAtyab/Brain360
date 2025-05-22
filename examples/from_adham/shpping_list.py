

falcon_list = [] 

def add():
  x = input("Enter item to add: ")
  falcon_list.append(x)
  print("'" + x + "' was added\n")

def remove():
  if len(falcon_list)==0:
    print("Nothing in the list\n")
    return
  show()
  n = input("Enter item number to remove: ")
  if n.isdigit():
    n = int(n)-1
    if n>=0 and n<len(falcon_list):
      gone = falcon_list.pop(n)
      print("'" + gone + "' was removed\n")
    else:
      print("Invalid number\n")
  else:
    print("not a number\n")

def show():
    if falcon==[]:
        print("List is empty\n")
    else:
        print("My shopping list:")
        for i in range(len(falcon_list)):
            print(str(i+1)+". "+falcon_list[i])
        print("")

def clear():
    falcon_list.clear()
    print("List cleared!\n")

def my_shopping_list():
    print("Welcome to my shopping list manager :)")
    while True:
        print("1 - add")
        print("2 - remove")
        print("3 - show")
        print("4 - clear")
        print("5 - exit")
        pick = input("Choose: ")
        if pick=="1":
            add()
        elif pick=="2":
            remove()
        elif pick=="3":
            show()
        elif pick=="4":
            clear()
        elif pick=="5":
            print("Chau!")
            break
        else:
            print("wrong input\n")

my_shopping_list()

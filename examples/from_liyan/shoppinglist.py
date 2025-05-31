"this program is your personal shopping list you can add remove clear and show your list!!!!!!!"

shopping_list = []

def add_item():
    item = input("What item would you like to add? ")
    shopping_list.append(item)
    print(f"Added '{item}' to your list.")

def remove_item():
    item = input("Which item would you like to remove? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from your list.")
    else:
        print(f"'{item}' is not in the list.")

def clear_list():
    shopping_list.clear()
    print("Shopping list cleared!")

def show_list():
    if shopping_list:
        print("Here is your shopping list:")
        for item in shopping_list:
            print("-", item)
    else:
        print("Your shopping list is empty.")

def main():
    while True:
        user_choice = input("\nWelcome to your shopping list! Choose an option: 'add', 'remove', 'clear', 'show', or 'quit': ").lower()

        if user_choice == "add":
            add_item()
        elif user_choice == "remove":
            remove_item()
        elif user_choice == "clear":
            clear_list()
        elif user_choice == "show":
            show_list()
        elif user_choice == "quit":
            print("Goodbye! See you next time.")
            break
        else:
            print("Invalid option. Please choose again.")


main()

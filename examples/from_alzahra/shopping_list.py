# Welcome message and menu
print("Welcome to Shopping List Manager!")
print("1. Add item")
print("2. Remove item")
print("3. Show list")
print("4. Clear list")
print("5. Exit")

# Empty list to store shopping items
list_of_sh = []

# Start the main loop
while True: #Since it's always true, the loop keeps going forever.
    try: # used to catch errors in the program without crashing it.
        # Get user's choice
        op = int(input("Choose an option (1, 2, 3, 4, 5): "))

        # Option 1: Add item
        if op == 1:
            item = input("Enter an item to add: ")
            list_of_sh.append(item)
            print(f"{item} added to the list!") #Allows to insert variables directly in strings (f"{item}")

        # Option 2: Remove item
        elif op == 2:
            item = input("Enter an item to remove: ")
            if item in list_of_sh:
                list_of_sh.remove(item)
                print(f"{item} removed from the list!")
            else:
                print(f"{item} is not in the list.")

        # Option 3: Show list
        elif op == 3:
            print("Your Shopping List:")
            if len(list_of_sh) > 0: #This checks if the shopping list has at least one item in it.
                for item in list_of_sh: #This loop goes through each item in the list and it prints each one on a new line.
                    print(item)
            else:
                print("The list is currently empty.")


        # Option 4: Clear list
        elif op == 4:
            list_of_sh.clear()
            print("The list has been cleared!")

        # Option 5: Exit
        elif op == 5:
            print("Exiting Shopping List Manager. Goodbye!")
            break #stops the loop and ends the program.

        # Invalid option
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

    # If user enters non-integer input
    except ValueError: #is the specific error that occurs when try to convert something like "hello" into an integer or vise versa.
        print("Please enter a valid number (1-5).")

def add_details():
    added_name = str(input("Please enter the customer's name: "))
    added_email = input("Please enter the customer's email: ")
    added_phone_number = int(input("Please enter the customer's phone number: "))
    added_gender = input("Please enter the customer's gender: ")
    with open("database.txt", "a") as database:
        database.write(f"Name: {added_name}, Email: {added_email}, Phone: {added_phone_number}, Gender: {added_gender}\n")
    return


def show_all():
    with open("database.txt", "r") as database:
        print("")
        print("All Details:")
        for i in database:
            print(i, end = "")
            print("---")
    return


def remove_item(removed_detail):
    with open("database.txt", "r") as database:
        lines = database.readlines()

    with open("database.txt", "w") as database:
        for i in lines:
            if removed_detail not in i:
                database.write(i)
    return


def remove_all():
    open("database.txt", "w").close()
    return


print("Thank you for choosing us as a service provider.")

shop_owner_name = input("Please cloud you provide us with your good name: ")

print("")

print(f"Thank you {shop_owner_name.strip().title()}, by the way your name is amazing!!!")

print("")

database_name = input("Please cloud you provide us with the database name that you prefer: ")

print("")

database_name_assigned = False

while database_name ==  "":
    if not database_name:
        database_name = input("Please enter the database name: ")

    elif database_name  is not "":
        database_name_assigned = True

with open("database.txt", "x") as database:
    print(f"You have created a database successfuly and you database name is {database_name}")

print("")

while True:
    options = int(input("What Is next: \n"
        "1. Add new customer details. \n" 
        "2. Show the all customer details. \n"
        "3. Remove a cusomer details. \n"
        "4. Remove all details in the database. \n"
        "Please Pick a Number: "))

    if options == 1:
        add_details()

    elif options == 2:
        show_all()

    elif options == 3:
        removed_detail = input("Enter the cutomer's name that you want to delete: ")
        remove_item(removed_detail)

    elif options == 4:
        remove_all()

    elif options == "Done".lower():
        break
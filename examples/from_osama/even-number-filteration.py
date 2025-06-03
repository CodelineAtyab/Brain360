database = []
def list_of_int(database):
    even_numbers = []
    for i in database:
        if i % 2 == 0:
            even_numbers.append(i) 
    return even_numbers

is_even = True

while is_even:
    inputted_numbers = input("Please Enter the numbers only (Str and Bolean) are not exepted and enter (print) to show the even numbers: ").lower()

    if inputted_numbers != "print":
        database.append(int(inputted_numbers))

    if inputted_numbers == "print":
        print(database)
        print(f"The Even Numbers Are: {list_of_int(database)}")
        is_even = False

    if inputted_numbers == "print" and len(database) == 0:
        print("The List is Empty :(")

print("Thanks for your input :)")
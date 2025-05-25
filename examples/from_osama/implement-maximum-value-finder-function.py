database = []

def largest_number():
    large_number = database[0]
    for i in database:
        if i > large_number:
            large_number = i
    print(large_number)

inputted_numbers = input("Enter the numbers when you are done write (done) to print the largest number you entered: ")
if inputted_numbers == "done":
    print(None)
else:
    database.append(int(inputted_numbers))


while inputted_numbers != "done":
    inputted_numbers = input("Enter the numbers when you are done write (done) to print the largest number you entered: ")
    if inputted_numbers == "done":
        largest_number()
        break
    database.append(int(inputted_numbers))
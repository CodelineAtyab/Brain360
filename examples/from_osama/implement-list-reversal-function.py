database = []
reverse_database = []

def reverse(database):
    for i in database[::-1]:
        reverse_database.append(i)
    return reverse_database

while True:
    inputted_values = input("Enter the values and when you are done please write (Done): ").lower()

    if inputted_values != "done":
        database.append(inputted_values)

    elif inputted_values == "done" and  len(database) == 0:
        print("Empty")
        break        

    elif inputted_values == "done":
        print(reverse(database))
        break
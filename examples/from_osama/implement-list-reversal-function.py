databaselist = []
def reverse(databaselist):
    reverse_database = []
    for i in databaselist[::-1]:
        reverse_database.append(i)
    return reverse_database

while True:
    inputted_values = input("Enter the values and when you are done please write (Done): ").lower()

    if inputted_values != "done":
        databaselist.append(inputted_values)

    elif inputted_values == "done" and  len(databaselist) == 0:
        print("Empty")
        break        

    elif inputted_values == "done":
        print(databaselist)
        print(reverse(databaselist))
        break
database = []
element = ""

def freq(database, element):
    element = input("What is the element you want to count: ")
    count_of_element = database.count(element)
    print(f"The Element {element} occurrence {count_of_element} Times")
    return freq

while True:
    inputted_number = input("Enter the numbers and write (Done) when you finish to get the most occurrence numbers: ").lower()
    if inputted_number == "done" and len(database) == 0:
        print(0)
        break
    elif inputted_number == "done":
        print(database)
        freq(database, element)
        break
    database.append(inputted_number)
    
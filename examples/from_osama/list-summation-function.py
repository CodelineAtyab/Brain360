database = []

def sum_list_elements(database):
    sum_all = sum(database)             
    return sum_all

it_is_sum = True

while it_is_sum:
    inputted_numbers = input("Please enter the a number whole or float number BUT do not enter any strig when you done please enter (Done): ").lower()
    if inputted_numbers != "done":
        database.append(float(inputted_numbers))
        
    if inputted_numbers == "done":
        print(database)
        print(f"The Total is:", sum_list_elements(database))
        break
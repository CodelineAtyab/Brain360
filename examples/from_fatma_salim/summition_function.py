
def sum_list_elements(data_points):
    total_sum = 0
    for num in data_points:
        total_sum += num
    return total_sum

while True:
    user_input = input("Enter numbers separated by commas: ")

    if user_input == "":
        print("You didn't enter anything. Please try again list is empty") # check for empty list 
        continue

    parts = user_input.split(",")
    valid = True
    numbers = []

    for part in parts:
        part = part.strip()
        if part.replace(".", "", 1).isdigit() or (part.startswith("-") and part[1:].replace(".", "", 1).isdigit()):
            numbers.append(float(part))
        else:
            print("Invalid input:", part) # if mix data enter not only number 

            valid = False
            break

    if valid:
        print("Sum is:", sum_list_elements(numbers))
        break


def calculate_total(num_list):

    total_sum = 0
    for value in num_list:
        total_sum += value
    print("Total Sum:", total_sum)
    return total_sum

# Collect user numbers
user_numbers = []
entry = ""

while entry.lower() != "sum":
    entry = input("Enter a number or type 'sum' to sum it: ")
    if entry.lower() != "sum":
        try:
            number = float(entry)
            user_numbers.append(number)
        except ValueError:
            print("That's not a valid number. Try again.")

print("Numbers you entered:", user_numbers)

# Call the function
calculate_total(user_numbers)

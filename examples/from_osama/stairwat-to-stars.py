numbers_of_rows_and_columns = int(input("Please enter a positive number: "))

for i in range(numbers_of_rows_and_columns):
    for add_a_star in range(i + 1):
        print("*", end = " ")
    print(" ")
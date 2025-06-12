numbers_of_rows_and_columns = int(input("Please enter a positive number: "))

for _ in range(numbers_of_rows_and_columns):
    for i in range(numbers_of_rows_and_columns):
        print( "*", end = " ")
    print(" ")
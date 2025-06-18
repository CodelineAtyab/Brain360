num_rows = input("Enter number of rows: ")

num_rows = int(num_rows)

for step in range(1, num_rows + 1):
    number_line = ""
    for count in range(1, step + 1):
        number_line = number_line + str(count)
    print(number_line)

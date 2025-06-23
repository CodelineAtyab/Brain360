number_of_rows = int(input("enter the row number: "))
for row in range (number_of_rows):
    for space in range ( number_of_rows-row-1):
       print (" ", end="")
    for star_number in range (2 * row+ 1):
       print ("*", end="")
    print ("")  
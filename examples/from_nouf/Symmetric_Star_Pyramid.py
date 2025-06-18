counter = 1
rows = int(input("please enter a number of rows you want"))
while counter < rows :
    spaces = rows - counter
    stars = counter * 2 - 1
    print(" " * spaces + "*" * stars)
    counter = counter + 1
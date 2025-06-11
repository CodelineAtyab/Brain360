number_of_steps = int (input ("Enter the number of steps: "))
if number_of_steps > 0:
    for steps in range (1, number_of_steps + 1):
        print (" " * (number_of_steps - steps) + "#" * steps)

else:
    print ("Invalid Input")
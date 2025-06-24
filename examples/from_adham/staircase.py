stair_size = input("How many steps? ")

if stair_size == "":
    print("You didn’t type anything.")
else:
    if stair_size[0] == "-":
        print("Negative number not allowed.")
    else:
        only_numbers = "0123456789"
        valid = True
        for letter in stair_size:
            if letter not in only_numbers:
                valid = False

        if valid:
            number = int(stair_size)
            step = 1
            while step <= number:
                spaces = " " * (number - step)
                hashes = "#" * step
                print(spaces + hashes)
                step = step + 1
        else:
            print("That’s not a number.")
            

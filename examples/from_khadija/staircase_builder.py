while True:
    user_input = input("Please input a positive number for the staircase height [type 'done' to exit]: ")

    if user_input.lower() == "done":
        print("Exiting program.")
        break  # Exit the loop if user types 'done'

    # Check if the input is a positive integer
    if user_input.isdigit():
        height = int(user_input)
        if height > 0:
            # Generate the staircase pattern
            for i in range(1, height + 1):
                print(" " * (height - i) + "#" * i)
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Invalid input. Please enter a positive number or 'done'.")




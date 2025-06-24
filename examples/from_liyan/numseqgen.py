"This program generates a number seqence it fun"
while True:
    try:
        user_input = int(input("Write a positive number: "))
        if user_input <= 0:
            print("Please enter a positive number greater than zero.")
        else:
           
            for i in range(1, user_input + 1):
                for j in range(1, i + 1):
                    print(j, end="")
                print()
            break  
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

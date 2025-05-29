list_Even_numbers = []

while True:
    option = input("Enter either a number or 'exit': ")

    if option == 'exit':
        break

    number = int(option)
    if number % 2 == 0:
        print("The number is an even number =", number)
        list_Even_numbers.append(number)
    else:
        print("The number is not even!")

print("The list of even numbers:", list_Even_numbers)

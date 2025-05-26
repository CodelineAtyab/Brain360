list_Even_numbers = []

def even_number():
    number = int(input("Enter a number = "))
    if number % 2 == 0:
        print("The number is an even number =", number)
        list_Even_numbers.append(number)
    else:
        print("It's not an even number!")

even_number()
even_number() 
even_number() 
even_number() 
even_number() 
even_number()   

print("The list of even numbers:", list_Even_numbers)

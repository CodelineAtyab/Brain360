numbers = []

while True:
    num = input("Enter a number or ( done ) to exit: ")
    if num != "done":
        numbers.append(int(num))
    else:
        break
    
even_numbers = []

def even_number(even_numbers):
    if numbers == []:
        print("The list is empty")
        return None
    else:
        for n in numbers:
            if n % 2 == 0:
                even_numbers.append(n)
        print(f"even numbers: {even_numbers}")        
        return even_numbers

even_number(even_numbers)
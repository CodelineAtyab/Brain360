def extract_even_numbers(values):
    even_numbers = [] 
    index = 0  

    
    while index < len(values):
        current = values[index]  

        
        if current % 2 == 0:
            even_numbers.append(current)  

        index += 1  

    return even_numbers  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
even_only = extract_even_numbers(numbers)  
print("Original list:", numbers)
print("Even numbers:", even_only)
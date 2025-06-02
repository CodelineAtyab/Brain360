def get_even_numbers():

    numbers_list = []

    even_numbers=[]
    
    while True:
        numbers_from_user = input("write your list of number and done when you finish: ")

        if numbers_from_user == "done": 
           break
        numbers_from_user = int(numbers_from_user)
        numbers_list.append(numbers_from_user)

        if numbers_from_user % 2 == 0:
            even_numbers.append(numbers_from_user)

            print(f"even numbers list = {even_numbers}") 
         
        else:
          print("It is an Odd Number, Enter an Even Number") 
            
        

get_even_numbers()





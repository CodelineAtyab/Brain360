numbers = []

while True:
    num = input("Enter a number or ( done ) to exit: ")
    if num != "done":
        numbers.append(int(num))
    else:
        break

def even_number(even_numbers):
    listOfeven=[]
    for n in even_numbers:
      if n % 2 == 0:
        listOfeven.append(n) 
    return listOfeven       
             
   
   

print("The list",numbers)
print("The list ot even " , even_number(numbers))

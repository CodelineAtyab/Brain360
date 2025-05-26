numbers=[]
def even_number(numbers):
    n = int(input("enter the length of the list: "))
    for i in range(n):
        num = int(input("Enter a number: "))
        numbers.append(num)
    if numbers==[]:
        print("The list is empty")
    else:
        even_num=[]
        for num in numbers:
            if num % 2 == 0:
                even_num.append(num)
        print(even_num)
even_number(numbers)
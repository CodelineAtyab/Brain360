list_of_num = []

while True:
    i_said = input("Write down numbers and enter 'exist' to view even numbers: ")
    
    if i_said == 'exist':
        break
    
    number = int(i_said)
    list_of_num.append(number)
    print("Please enter a valid number or 'exist' to quit.")

for num in list_of_num:
    if num % 2 == 0:
        print("Even number:", num)


database = []

def largest_number():
    max_num = database[0]
    

numbers_input = int(input("Enter the numbers and when you are done write (done) to get the largest number: "))

while numbers_input != "done":
    numbers_input = int(input("Enter the numbers and when you are done write (done) to get the largest number: "))
    database.append(numbers_input)
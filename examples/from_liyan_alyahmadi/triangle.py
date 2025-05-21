#declartation

number= 1

#input
user_input = int(input("Please writ your number to create a triangle: "))

#process input
for i in range(1, user_input+1):
    print(' '*(user_input-i) + '1' *i + ' ' + '1'*i)
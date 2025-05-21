num = int(input("Enter a number: "))

if num>0:
  for i in range(1,num+1):
    print((' '*(num-i)+(i*'#')))
else:
    print("Enter a positive number")
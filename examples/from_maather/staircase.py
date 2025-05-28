num = int(input("enter number of rows:"))
if num > 0:
    for i in range(1,num+1):
        print(" " *(num -i)+"#" * i)
else:
   print("invalid")
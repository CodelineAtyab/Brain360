num = int(input("Enter the number of row:"))
for i in range(num):
   space = num - i - 1
   star = 2 * i + 1
   print(" " * space + "*" * star)


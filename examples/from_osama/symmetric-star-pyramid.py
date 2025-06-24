count = int(input("Enter a positive number: "))

for i in range(1, count + 1):
        print( " " * (count - i) + "*" * (2 * i - 1))

num = int(input())

for i in range(num):
    print((" " * (num - i) + "*" * i) + ("" * (num - i) + "*" * i) + ("" * (num) + "*"))
print()
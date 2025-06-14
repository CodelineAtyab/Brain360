height = int(input("Enter the height of the staircase: "))

if height<0:
    print("Enter positive number!")

else:

    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        hashes = '#' * i
        print(spaces + hashes)
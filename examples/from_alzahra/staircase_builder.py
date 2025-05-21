height = int(input("Enter the height of the staircase (positive integer): "))

if height<0:
    print("Error: Please enter a positive integer greater than 0.")

else:
# Loop to generate each row of the staircase
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        hashes = '#' * i
        print(spaces + hashes)

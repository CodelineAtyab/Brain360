
size = input("How many stars? ")

size = int(size)

for row in range(size):
    stars = ""
    for star_count in range(size):
        stars = stars + "*"
    print(stars)


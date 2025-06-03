def flip_list(start_list):
    backward_list = []
    spot = len(start_list) - 1
    while spot >= 0:
        backward_list.append(start_list[spot])
        spot = spot - 1
    return backward_list

user_line = input("Write your stuff, split with commas: ")
split_things = user_line.split(",")

result = flip_list(split_things)

print("What you typed:", split_things)
print("Flipped around:", result)

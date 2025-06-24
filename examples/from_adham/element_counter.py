def how_many_times(data_list, thing_to_find):
    total = 0
    for stuff in data_list:
        if stuff == thing_to_find:
            total = total + 1
    return total


raw_input = input("Type things with commas in between: ")
my_list = raw_input.split(",")


what_to_look_for = input("What do you want to count? ")


count = how_many_times(my_list, what_to_look_for)
print("It showed up", count, "times.")

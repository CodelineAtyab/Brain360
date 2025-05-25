
first_list = []

def black_list():
    global second_list
    second_list = first_list[::-1]
    return second_list

print("Please enter you list items: ")
user_input = input()
while user_input != "done":
    first_list.append(user_input)
    user_input = input()

black_list()
print("Your list items: ")
print(first_list)
print("Your reversed list items: ")
print(second_list)
print("Your reversed list items in order:")
for item in second_list:
    print(item)




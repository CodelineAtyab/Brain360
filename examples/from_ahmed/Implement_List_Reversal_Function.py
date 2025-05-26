
first_list = []
second_list = []

def re_list(re):
    return re[::-1]

print("Please enter you list items, type 'done' once finished: ")
user_input = input()
while user_input != "done":
    first_list.append(user_input)
    user_input = input()

second_list = re_list(first_list)
print("Your list items: ")
print(first_list)
print("Your reversed list items: ")
print(second_list)
print("Your reversed list items in order:")
for item in second_list:
    print(item)
    
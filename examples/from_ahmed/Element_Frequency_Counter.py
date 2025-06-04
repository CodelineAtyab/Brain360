

freq_list = []

def freq(nums_list, elment_count):

    count = 0
    new_list = []

    for item in nums_list:
        count = 0
        for data in nums_list:
            if item == data:
                count = count + 1
                new_list.append((f"The item: {item}", f"The frequncy: {count}"))
    return new_list

print("Enter a set of even and odd numbers and type 'done' once finished")
user_input = input()
el_count = 0
if user_input == '':
    print(freq_list)
else:
    while user_input != "done": 
        freq_list.append(user_input)
        user_input = input()


print("Your list of numbers and elemnt frequncy: ")
final_list = freq(freq_list, el_count)
print(final_list)
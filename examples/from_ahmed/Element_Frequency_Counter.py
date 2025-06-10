
freq_list = []


def freqc(data_list):
    frequency_result = {}
    for item in data_list:
        if item in frequency_result:
            frequency_result[item] += 1
        else:
            frequency_result[item] = 1
    return frequency_result


print("Enter your elements and type 'done' once finished")
user_input = input()

while user_input != "done":
    freq_list.append(user_input)
    user_input = input()

freqs = freqc(freq_list)

print("Your list of elements and their frequencies:")
print(freq_list)
for element, count in freqs.items():
    print(f"the frequncy of {element}", f"is {count}")

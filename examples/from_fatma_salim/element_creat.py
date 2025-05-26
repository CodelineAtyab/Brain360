def count_element_occurrences(data_list, element_to_count):
    count = 0
    for item in data_list:
        if item == element_to_count:
            count += 1
    return count

print("Let's build your list one item at a time.")
data_list = []

n = int(input("How many items do you want in the list? "))


for i in range(n):
    item = input(f"Enter item {i+1}: ")
    data_list.append(item)


element_to_count = input("Enter the element you want to count: ")

print("Output:", count_element_occurrences(data_list, element_to_count))
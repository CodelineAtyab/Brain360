'''def count_element(data_list, count_data):
    count = 0
    for item in data_list:
        if item == count_data:
            count += 1
    return count


user_input = input("Enter the list items separated by commas (e.g., a,b,a,c): ")
data_list = user_input.split(",")


count_data = input("Enter the element you want to count: ")


result = count_element(data_list, count_data)
print(f"The element '{count_data}' appears {result} time(s) in the list.")
'''

def count_element_occurrences(data_list, element_to_count):
    count = 0
    for item in data_list:
        if item == element_to_count:
            count += 1
    return count


print("Enter list items one by one. Type 'done' when finished:")

data_list = []
while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    data_list.append(item)


element_to_count = input("Enter the element you want to count: ")


result = count_element_occurrences(data_list, element_to_count)
print(f"The element '{element_to_count}' appears {result} time(s) in the list.")

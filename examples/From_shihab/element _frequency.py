def count_element_occurrences(data_list, element_to_count):
    count = 0
    for item in data_list:
        if item == element_to_count:
            count += 1
    return count




data_list = []
while True:
    item = input("Enter list items one by one. Type 'done' when finished:")
    if item.lower() == "done":
        break
    data_list.append(item)


element_to_count = input("Enter the element you want to count: ")

result = count_element_occurrences(data_list, element_to_count)
print(f"The element '{element_to_count}' appears {result} time(s) in the list.")
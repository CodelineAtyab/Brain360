#Create Element Frequency Counter Functio

def count_element_occurrences(data_list, element_to_count):
    count = 0
    for item in data_list:
        if item == element_to_count:
            count += 1
    return count


data = ["c", "b", "a", "c", "c", "a"]
numbers = [1, 2, 3, 4, 5]
empty_collection = []

print(count_element_occurrences(data, "c"))           
print(count_element_occurrences(numbers, 8))             
print(count_element_occurrences(empty_collection, "x"))  

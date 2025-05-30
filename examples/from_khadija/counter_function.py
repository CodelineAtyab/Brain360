
def count_element_occurrences(my_list, item_to_count):
    count = 0  
    for item in my_list:
        if item == item_to_count:
            count += 1  
    return count  

my_data = ["a", "b", "a", "c", "a", "a"]
print("List:", my_data)
print("How many times 'a' appears:", count_element_occurrences(my_data, "a"))  

numbers = [1, 2, 3, 4, 5]
print("List:", numbers)
print("How many times '7' appears:", count_element_occurrences(numbers, 7))  

empty_list = []
print("List:", empty_list)
print("How many times 'x' appears:", count_element_occurrences(empty_list, "x"))  
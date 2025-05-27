#DECLARATION
def count_element(input_list, element):
    """
    This function takes a list and a specified element, and returns the count of that element in the list.
    If the element is not in the list, it returns 0.
    """
    count = 0
    for i in input_list:
        if i == element:
            count += 1
    return count

#INPUT
user_list_input = input("Enter a list of elements separated by spaces: ")
#PROCESS INPUT
user_list = user_list_input.strip().split()


element_input = input("Enter the element you want to count: ")


result = count_element(user_list, element_input)
#PRINT
print(f"The element '{element_input}' appears {result} times in the list.")

def count_element_occurr(data_list, element_to_count):
    count = 0
    for item in data_list:
        if item == element_to_count:
            count += 1
    return count


user_input = input("Enter list items separated by commas : ") #enter word without space only comma
data_list = user_input.split(',') # spilt between word by comma 

element_to_count = input("Enter the element you want to count: ")

result = count_element_occurr(data_list, element_to_count) # call function

print("Output:", result)
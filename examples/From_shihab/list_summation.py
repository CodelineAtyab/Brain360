def sum_list_elements(number_list):
    return sum(number_list)


print("Enter numbers one by one. Type 'done' when finished:")

number_list = []
while True:
    num = input("Number: ")
    if num.lower() == "done":
        break
    number_list.append(float(num))  


result = sum_list_elements(number_list)
print("The sum of the numbers is:", result)
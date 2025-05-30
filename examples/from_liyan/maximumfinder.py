def finding_max_value(num):
   
    if not num:
        return None


    max_value = num[0]

    for value in num[1:]:
        if value > max_value:
            max_value = value

    return max_value


user_input = input("Enter a list of numbers separated by spaces then press enter to view the maximum: ")

numbers = [float(num) for num in user_input.strip().split()]
max_value = finding_max_value(numbers)
if max_value is not None:
    print("The maximum value is:", max_value)
else:
    print("The list is empty!!!")



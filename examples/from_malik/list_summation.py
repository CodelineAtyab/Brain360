def sum_list_elements(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

input_list = []

while True:
    user_input = input("Enter numbers separated by commas (or 'done' to finish): ")
    
    if user_input.strip().lower() == "done":
        print("Final sum:", sum_list_elements(input_list))
        break
    
    if user_input.strip() == "":
        print(f"Current sum: {sum_list_elements(input_list)}")
        continue

    try:
        new_numbers = [float(num.strip()) for num in user_input.split(",")]
        input_list.extend(new_numbers)
        print(f"Current sum: {sum_list_elements(input_list)}")
    except ValueError:
        print("Please enter only valid numbers separated by commas.")
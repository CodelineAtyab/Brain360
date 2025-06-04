list_of_nums = []

while True:
    user_input = input("Enter the numbers write(done) to exit: ")
    if user_input != "done":
        list_of_nums.append(int(user_input))
    else:
        break

def find_max_value(list_of_nums):
    if list_of_nums == []:
        print("List is empty")
        return None
    else:
        maximum = list_of_nums[0]
        for i in list_of_nums:   
            if i > maximum:
                maximum = i
        return maximum
               

           

print("The maximim valus is: ",find_max_value(list_of_nums))                


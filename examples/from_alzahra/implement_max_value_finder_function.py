# Step 1: Create the list to store the numbers that entered by the user
list_max_value=[]

# Step 2: Define the function
def find_max_value(list_max_value):
    while True:
        number=input("Enter a number or (done) to exit:")
        if number == 'done':
            if list_max_value == []:
                return None 
            else:
                print("Original List : " ,list_max_value)
                return max_value
                break
        else:
            list_max_value.append(int(number))
            max_value=list_max_value[0] 

            for num in list_max_value:
                if num>max_value:
                    max_value=num  
    

result=find_max_value(list_max_value)
print(f"the maximum number of the {list_max_value} is : {result}")
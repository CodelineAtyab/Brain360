# Step 1: Create the list to store the numbers that entered by the user
list_max_value=[]
# Ask for number of elements
element_num=int(input("Enter the numbet of elements in the list : "))

# Get elements from the user

for i in range (element_num):
    number=int(input("Enter a number :"))
    list_max_value.append(number)

print("Original List : " ,list_max_value)

# Step 2: Define the function
def find_max_value(list_max_value):
    #step2.1: we will define an if statement to return an empty list if their is no number entered by the user
    if not list_max_value:
        return None #this will return an empty list in case the user didn't enter nothing in the list
    #step2.2: we will assume that the 1st number that'll be entered by the user in the list is tha maximum number 
    #to compare and go through each number in the list to find the max number
    max_value=list_max_value[0] #the 1st number in the list is the Max number
    for num in list_max_value:
        if num>max_value:
            max_value=num #the new number now is the max num in case if it is larger than the 1st num in the list
    return max_value

result=find_max_value(list_max_value)
print(f"the maximum number of the {list_max_value} is : {result}")

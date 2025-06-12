# Step 1: Create the list to store the numbers that entered by the user
list_x=[]
# Ask for number of elements
element_num=int(input("Enter the numbet of elements in the list : "))

# Get elements from the user
for i in range (element_num):
    number=int(input("Enter a number :"))
    list_x.append(number)

print("Original List : " ,list_x)

# Step 2: Define the function
def get_even_numbers(list_x):
    new_list=[]
    for num in list_x:
        if num%2==0:
            new_list.append(num)
    return new_list #Outside the loop to go through all the integers in the list and print out only the even numbers in a new list
    
# Step 3: Call the function and print result
result=get_even_numbers(list_x)
print(f"The Even Number List : {result}")

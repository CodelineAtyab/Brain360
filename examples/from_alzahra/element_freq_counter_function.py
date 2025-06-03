# Step 1: Create the list to store the numbers that entered by the user
list_of_el=[]
# Ask for number of elements
element_num=int(input("Enter the numbet of elements in the list : "))
element_to_count=input("Enter the element you need to count:")

# Get elements from the user
for i in range (element_num):
    element=input("Enter an element :")
    list_of_el.append(element)

print("Original List : " ,list_of_el)

# Step 2: Define the function
def count_element_occurrences(element_to_count,list_of_el):
    count=0
    for num in list_of_el:
        if num==element_to_count:
            count+=1
    return count
    
# Step 3: Call the function and print result
result=count_element_occurrences(element_to_count,list_of_el)
print(f"number of the {element_to_count} is : {result}")